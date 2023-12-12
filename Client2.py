import socket
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def sending_login(self):
        self.switch_window.emit(self.lineEdit.text())
        text = self.lineEdit.text()
        chatapp = ChatApplication()
        chatapp.send_login(text)

    def __init__(self):
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

        self.setWindowTitle("Form")
        self.pushButton.setText("Connexion")
        self.label.setText( "Connexion au serveur")
        self.label_2.setText( "Entre votre pseudo")

class chat(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setObjectName("Form")
        self.resize(1128, 630)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(840, 580, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(302, 580, 541, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(170, 10, 801, 551))
        self.textEdit.setObjectName("textEdit")

        self.setWindowTitle("Form")
        self.pushButton.setText( "Envoyer")

class ChatApplication(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.client_socket = socket.socket()
        self.client_socket.connect(('127.0.0.1', 12345))

        self.send_thread = threading.Thread(target=self.send_message)
        self.receive_thread = threading.Thread(target=self.message_received)

        self.send_thread.start()
        self.receive_thread.start()

    def showfen1(self):
        self.fen1 = login()
        self.fen1.switch_window.connect(self.showfen2)
        self.fen1.show()


    def showfen2(self):
        self.fen2 = chat()
        self.fen2.show()

    def send_login(self, send):
        message = send
        self.client_socket.send(message.encode())

    def send_message(self):
        try:
            while True:
                message = input("-> ")
                self.client_socket.send(message.encode())

        finally:
            self.client_socket.close()

    def message_received(self):
        while True:
            response = self.client_socket.recv(100)
            print(f"\n{response.decode()}")
            if response.lower() == 'bye':
                break

    def send_button_clicked(self):
        message = self.lineEdit.text()
        self.textEdit.append(f"{message}")
        self.client_socket.send(message.encode())
        self.lineEdit.clear()



def main():
    app = QtWidgets.QApplication(sys.argv)
    chat_app = ChatApplication()
    chat_app.showfen1()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()


