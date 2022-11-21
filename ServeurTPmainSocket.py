import sys
import socket

host = ""
port = 7777

def Serveur():
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    while True:
        conn, address = server_socket.accept()

        data = ""


        while data != "exit" and data != "bye":
            data = conn.recv(1024).decode()
            print(data)
            reply = input("Réponse:")
            conn.send(reply.encode())

        conn.close()


if __name__ == '__main__':
    sys.exit(Serveur())