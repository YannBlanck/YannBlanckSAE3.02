import socket
import threading

def send_message(sock):
    try:
        while True:
            message = input("-> ")
            sock.send(message.encode())

            if message.lower() == 'bye':
                break
    finally:
        sock.close()

def message_reçue(sock):
    while True:
        response = sock.recv(100)
        print(f"\n{response.decode()}")
        if response.lower() == 'bye':
            break

def main():
    client_socket = socket.socket()
    client_socket.connect(('127.0.0.1', 12345))

    try:
        send_thread = threading.Thread(target=send_message, args=(client_socket,))
        receive_thread = threading.Thread(target=message_reçue, args=(client_socket,))
        send_thread.start()
        receive_thread.start()
        send_thread.join()
        receive_thread.join()
    except KeyboardInterrupt:
        print("Déconnexion du client.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    main()
