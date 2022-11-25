import sys
import socket

host = ""
port = 7777

def Serveur():
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    data = ""
    reply = ""
    while True:
        conn, address = server_socket.accept()

        if data == "exit" or data == "bye":
            break

        while data != "exit" and data != "bye" and reply != "exit" and reply != "bye":
            data = conn.recv(1024).decode()
            print(data)
            reply = input("Réponse:")
            conn.send(reply.encode())



        conn.close()


if __name__ == '__main__':
    sys.exit(Serveur())