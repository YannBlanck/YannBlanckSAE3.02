import socket
import threading
import time
import mysql.connector

# Liste pour stocker les connexions des clients et leurs identifiants
clients = {}
ban = {}
kick = {}
heur = {}

# Initialiser la connexion à la base de données MySQL
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="toto",
    database="serveurchat"
)
db_cursor = db_connection.cursor()

# Créer la table messages si elle n'existe pas
db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS messages (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user VARCHAR(255),
        message TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
''')

db_cursor.execute('''
    CREATE TABLE IF NOT EXISTS utilisateurs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nom VARCHAR(255)
    )
''')
db_connection.commit()

def save_message(user, message):
    # Sauvegarder le message dans la base de données
    db_cursor.execute("INSERT INTO messages (user, message) VALUES (%s, %s)", (user, message))
    db_connection.commit()

def commande(serv):
    global clients
    global ban

    while True:
        command = input()
        comm = command[:3]
        com = command[:4]
        user=""
        if command.lower() ==  "kill":

            for client in clients.keys():
                client.close()
                serv.close()
            break

        elif comm.lower() == "ban":
            user = command[4:]
            for client_id in clients:
                if client_id == user:
                    ban[client] = client_id
                    client.close()
                    break

        elif com.lower() == "kick":
            user = command[5:]
            for client_socket, id in clients.items():
                if id == user:
                    kick[client_socket] = time.time() + 360  # Bloquer le client pour 60 secondes
                    break
        else:
            print(f"commande inconnue: {command}")


def broadcast(message, sender):
    for client, client_id in clients.items():
        # Ne pas envoyer le message à l'expéditeur d'origine
        if client != sender:
            try:
                client_name = clients[sender]
                client.send(f"{client_name}: {message}".encode())
            except:
                # En cas d'erreur, supprimer le client de la liste
                remove_client(client)

def remove_client(client):
    if client in clients:
        client_id = clients.pop(client)
        print(f"Client {client_id} déconnecté.")
        client.close()

def inscription(client, client_id):
    global db_cursor
    global db_connection

    try:
        # Vérifier si l'utilisateur existe déjà dans la base de données
        db_cursor.execute("SELECT id FROM utilisateurs WHERE nom = %s", (client_id,))
        result = db_cursor.fetchone()

        if result:
            client.send("Cet identifiant est déjà utilisé. Veuillez en choisir un autre.".encode())
            return

        # Insérer l'utilisateur dans la base de données
        db_cursor.execute("INSERT INTO utilisateurs (nom) VALUES (%s)", (client_id,))
        db_connection.commit()

        client.send("Inscription réussie! Vous pouvez maintenant envoyer des messages.".encode())
    except Exception as e:
        print(f"Erreur lors de l'inscription : {e}")
        client.send("Une erreur s'est produite lors de l'inscription.".encode())

def message_inscription(client, address):
    client_id = client.recv(1024).decode()
    clientident = client_id.strip()[12:]
    inscript = client_id[:11]
    #print(client_id)
    #print(clientident)
    #print(inscript)

    # Vérifier si le message est une demande d'inscription
    if inscript.lower() == "inscription":
        inscription(client, clientident)
        return

def message_connexion(client, address):
    client_id = client.recv(1024).decode()
    client_name = client_id.strip()[10:]
    connexion = client_id[:9]

    # Vérifier si l'utilisateur est inscrit dans la base de données
    db_cursor.execute("SELECT id FROM utilisateurs WHERE nom = %s", (client_name,))
    result = db_cursor.fetchone()
    #print(result)

    if not result:
        client.send("Vous n'êtes pas inscrit. Veuillez vous inscrire pour accéder au chat.".encode())
        return
    try:
        if result:
            clients[client] = client_name
            print(f"Nouveau client connecté: {client_name}")

            while True:
            # Recevoir un message du client
                message = client.recv(1024)
                print(f"{client_name}, {message.decode()}")
                if not message:
                    break

                save_message(client_name, message.decode())

                # Diffuser le message à tous les clients connectés
                broadcast(message.decode(), client)
                #print(message.decode())
    except ConnectionResetError:
        # Le client s'est déconnecté de manière inattendue
        print("Client déconnecté de manière inattendue.")
    finally:
        # Gérer la déconnexion du client
        handle_disconnection(client)


def handle_disconnection(client_socket):
    global clients

    # Récupérer le nom du client déconnecté
    disconnected_client = clients.get(client_socket)

    if disconnected_client:
        print(f"Client déconnecté: {disconnected_client}")
        remove_client(client_socket)
    else:
        print("Erreur lors de la déconnexion : client non trouvé.")

def handle_client(client, address):

    message_connexion(client, address)

    message_inscription(client, address)

def main():
    global clients

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(5)
    #print(server_socket)

    commande_thread = threading.Thread(target=commande, args=(server_socket,))
    commande_thread.start()

    print("Serveur activé sur 127.0.0.1:12345")

    try:
        while True:
            # Accepter une connexion client
            client_socket, address = server_socket.accept()

            if client_socket in kick and time.time() < kick[client_socket]:
                print("Client kické. Attendez un moment avant de vous reconnecter.")
                client_socket.close()
                continue

            # Gérer le client dans un thread distinct
            client_thread = threading.Thread(target=handle_client, args=(client_socket,address))
            client_thread.start()

    except KeyboardInterrupt:
        print("Arrêt du serveur.")
    finally:
        # Fermer le socket du serveur
        server_socket.close()

        db_cursor.close()
        db_connection.close()

if __name__ == "__main__":
    main()