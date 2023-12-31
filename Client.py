import socket
import threading
from PyQt5 import QtCore, QtWidgets
import sys

"""
Application de discussion avec interface graphique (GUI) en PyQt5

Ce script crée une application de chat où les utilisateurs peuvent se connecter, s'inscrire,
et échanger des messages avec un serveur distant.

Classes :
- Login : Fenêtre de connexion pour saisir le nom d'utilisateur et l'adresse IP du serveur.
- Chat : Fenêtre principale de chat permettant l'envoi et la réception de messages.
- Inscription : Fenêtre d'inscription pour créer un nouveau compte utilisateur.
- ChatApplication : Gère le flux global de l'application, y compris la connexion au serveur.

Fonctions :
- main : Point d'entrée du script, initialise l'application PyQt et l'instance ChatApplication.
"""


class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str, str)

    def sending_login(self):
        username = self.lineEdit.text()
        ip_address = self.ipLineEdit.text()
        self.switch_window.emit(username, ip_address)
        login_data = f"connexion {username}"
        self.send_message(login_data)

    def open_inscription(self):
        self.fenisnc = Inscription(send_message_func=self.send_message)
        self.fenisnc.inscription_signal.connect(self.switch_window)
        self.fenisnc.show()

    def __init__(self, send_message_func):
        QtWidgets.QWidget.__init__(self)

        self.feninsc = Inscription(send_message_func=send_message_func)

        self.setObjectName("log")
        self.resize(428, 167)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 110, 241, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(280, 110, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sending_login)

        self.inscbutton = QtWidgets.QPushButton(self)
        self.inscbutton.setGeometry(QtCore.QRect(280, 69, 75, 31))
        self.inscbutton.setObjectName("inscbutton")
        self.inscbutton.clicked.connect(self.open_inscription)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 10, 121, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 121, 16))
        self.label_2.setObjectName("label_2")

        # Add a QLineEdit for IP address input
        self.ipLineEdit = QtWidgets.QLineEdit(self)
        self.ipLineEdit.setGeometry(QtCore.QRect(30, 30, 241, 31))
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.ipLineEdit.setPlaceholderText("Enter Server IP")

        # Utilisation d'un layout vertical
        layout = QtWidgets.QVBoxLayout(self)

        # Ajout des widgets au layout
        layout.addWidget(self.label)
        layout.addWidget(self.label_2)
        layout.addWidget(self.ipLineEdit)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.inscbutton)

        self.send_message = send_message_func

        self.setWindowTitle("Login")
        self.pushButton.setText("Connexion")
        self.label.setText("Connexion au serveur")
        self.label_2.setText("Entre votre pseudo")
        self.inscbutton.setText("Inscription")

class Chat(QtWidgets.QWidget):
    message_signal = QtCore.pyqtSignal(str)
    disconnect_signal = QtCore.pyqtSignal()

    def sending_text(self):
        text = self.line.text()
        self.message_signal.emit(text)
        self.send_message(text)

    def disconnect(self):
        self.disconnect_signal.emit()

    #def change_channel(self):
        #channel=self.channel_combobox.currentText()
        # Envoyer un message spécial pour indiquer le changement de salon
        #self.send_message(f"/join {channel}")

    def __init__(self, send_message_func):
        QtWidgets.QWidget.__init__(self)

        self.setObjectName("Form")
        self.resize(1128, 630)
        self.send_message = send_message_func

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(840, 580, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Envoyer")
        self.pushButton.clicked.connect(self.sending_text)

        self.line = QtWidgets.QLineEdit(self)
        self.line.setGeometry(QtCore.QRect(302, 580, 541, 31))
        self.line.setObjectName("lineEdit")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(170, 10, 801, 551))
        self.textEdit.setObjectName("textEdit")

        self.disconnect_button = QtWidgets.QPushButton(self)
        self.disconnect_button.setGeometry(QtCore.QRect(10, 580, 81, 31))
        self.disconnect_button.setObjectName("disconnect_button")
        self.disconnect_button.setText("Déconnexion")
        self.disconnect_button.clicked.connect(self.disconnect)

        #self.channel_combobox = QtWidgets.QComboBox(self)
        #self.channel_combobox.setGeometry(QtCore.QRect(100, 580, 120, 31))
        #self.channel_combobox.setObjectName("channel_combobox")
        #self.channel_combobox.addItem("General")
        #self.channel_combobox.addItem("Blabla")
        #self.channel_combobox.addItem("Comptabilite")
        #self.channel_combobox.addItem("Informatique")
        #self.channel_combobox.addItem("Marketing")
        #self.channel_combobox.currentIndexChanged.connect(self.change_channel )

        # Utilisation d'un layout vertical
        layout = QtWidgets.QVBoxLayout(self)

        # Ajout des widgets au layout
        layout.addWidget(self.textEdit)
        #layout.addWidget(self.channel_combobox)
        layout.addWidget(self.line)
        layout.addWidget(self.pushButton)
        layout.addWidget(self.disconnect_button)

        self.setWindowTitle("CHAT SAE")

class Inscription(QtWidgets.QWidget):
    inscription_signal = QtCore.pyqtSignal(str, str)

    def sending_inscription(self):
        username = self.lineEdit.text()
        ip_address = self.ipLineEdit.text()

        registration_data = f"inscription {username}"
        print(f"envoyer {registration_data}")
        self.inscription_signal.emit(registration_data, ip_address)
        self.send_message(registration_data)
        self.close()

    def send_inscription_data(self, username, ip_address):
        self.connect_to_server(username, ip_address)

    def __init__(self, send_message_func):
        QtWidgets.QWidget.__init__(self)

        self.send_message = send_message_func
        self.setObjectName("log")
        self.resize(428, 167)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 110, 241, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.ipLineEdit = QtWidgets.QLineEdit(self)
        self.ipLineEdit.setGeometry(QtCore.QRect(30, 30, 241, 31))
        self.ipLineEdit.setObjectName("ipLineEdit")
        self.ipLineEdit.setPlaceholderText("Enter Server IP")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(280, 110, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sending_inscription)

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 10, 121, 16))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 121, 16))
        self.label_2.setObjectName("label_2")

        layout = QtWidgets.QVBoxLayout(self)

        # Ajout des widgets au layout
        layout.addWidget(self.label)
        layout.addWidget(self.label_2)
        layout.addWidget(self.ipLineEdit)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.pushButton)

        self.send_message = send_message_func

        self.setWindowTitle("Inscritpion")
        self.pushButton.setText("Inscription")
        self.label.setText("Inscription au serveur")
        self.label_2.setText("Entrez votre pseudo")


class ChatApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.showfen1()

    def connect_to_server(self, TEXT, ip_address):
        if ip_address:
            print(ip_address)

            self.client_socket = socket.socket()
            try:
                self.client_socket.connect((ip_address, 12345))
                if TEXT[:11] == "inscription":
                    self.send_message(TEXT)

                self.showfen2(TEXT)
            except Exception as e:
                print(f"Error connecting to the server: {e}")


    def showfen1(self):
        self.fen1 = Login(send_message_func=self.send_message)
        self.fen1.switch_window.connect(self.connect_to_server)
        self.fen1.show()

    def showinsc(self):
        self.fenisnc = Inscription(send_message_func=self.send_message)
        self.fenisnc.inscription_signal.connect(self.connect_to_server)
        self.fenisnc.show()

    def showfen2(self, username):
        self.fen1.close()
        self.fenisnc.close()

        self.fen2 = Chat(send_message_func=self.send_message)
        self.fen2.message_signal.connect(self.message)
        self.fen2.disconnect_signal.connect(self.disconnect_client)

        self.send_thread = threading.Thread(target=self.receive_messages)
        self.send_thread.start()

        self.fen2.show()

    def receive_messages(self):
        while True:
            response = self.client_socket.recv(100)
            print(f"\n{response.decode()}")
            self.fen2.textEdit.append(response.decode())
            if response.lower() == 'bye':
                break

    def message(self, message):
        self.fen2.textEdit.append(f"{message}")
        self.fen2.line.clear()

    def send_message(self, message):
        self.client_socket.send(message.encode())

    def disconnect_client(self):
        # Ferme la fenêtre de chat
        self.fen2.close()

        # Termine le programme
        QtWidgets.QApplication.quit()
        reponses = "bye"

        # Arrête le thread
        self.send_thread.quit()
        self.send_thread.wait()

def main():
    app = QtWidgets.QApplication(sys.argv)
    chat_app = ChatApplication()
    chat_app.showfen1()
    chat_app.showinsc()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
