import socket
import threading
from PyQt5 import QtCore, QtWidgets
import sys

class Login(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def sending_login(self):
        username = self.lineEdit.text()
        self.switch_window.emit(username)
        self.send_message(username)  # Send the login message

    def __init__(self, send_message_func):
        QtWidgets.QWidget.__init__(self)

        self.setObjectName("log")
        self.resize(428, 167)
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 110, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(280, 110, 75, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.sending_login)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(150, 10, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 121, 16))
        self.label_2.setObjectName("label_2")

        self.send_message = send_message_func  # Reference to the message sending function

        self.setWindowTitle("Form")
        self.pushButton.setText("Connexion")
        self.label.setText("Connexion au serveur")
        self.label_2.setText("Entre votre pseudo")

class Chat(QtWidgets.QWidget):
    message_signal = QtCore.pyqtSignal(str)

    def sending_text(self):
        text = self.line.text()
        self.message_signal.emit(text)
        self.send_message(text)  # Send the message

    def __init__(self, send_message_func):
        QtWidgets.QWidget.__init__(self)

        self.setObjectName("Form")
        self.resize(1128, 630)
        self.send_message = send_message_func

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(840, 580, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.line = QtWidgets.QLineEdit(self)
        self.pushButton.clicked.connect(self.sending_text)
        self.line.setGeometry(QtCore.QRect(302, 580, 541, 31))
        self.line.setObjectName("lineEdit")

        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(170, 10, 801, 551))
        self.textEdit.setObjectName("textEdit")

        self.setWindowTitle("Form")
        self.pushButton.setText("Envoyer")

class SendMessagesThread(threading.Thread):
    def __init__(self, client_socket, chat_widget):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.chat_widget = chat_widget

    def run(self):
        try:
            while True:
                message = input("-> ")
                self.client_socket.send(message.encode())
                self.chat_widget.textEdit.append(f"{message}")
        finally:
            self.client_socket.close()

class ChatApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.client_socket = socket.socket()
        self.client_socket.connect(('127.0.0.1', 12345))

        self.fen2 = Chat(send_message_func=self.send_message)
        self.fen2.message_signal.connect(self.receive_message)

        self.send_thread = threading.Thread(target=self.receive_messages)
        self.send_thread.start()

    def showfen1(self):
        self.fen1 = Login(send_message_func=self.send_message)
        self.fen1.switch_window.connect(self.showfen2)
        self.fen1.show()

    def showfen2(self, username):
        self.fen1.close()
        self.fen2.show()

    def receive_messages(self):
        while True:
            response = self.client_socket.recv(100)
            print(f"\n{response.decode()}")
            self.fen2.textEdit.append(response.decode())
            if response.lower() == 'bye':
                break

    def receive_message(self, message):
        self.fen2.textEdit.append(f"{message}")
        self.fen2.line.clear()

    def send_message(self, message):
        self.client_socket.send(message.encode())


def main():
    app = QtWidgets.QApplication(sys.argv)
    chat_app = ChatApplication()
    chat_app.showfen1()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
