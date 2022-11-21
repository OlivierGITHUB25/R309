import sys
import socket

host = "192.168.197.1"
port = 7777

def Client():
    client_socket = socket.socket()
    client_socket.connect((host, port))
    message = ""

    while message != "exit" and message != "bye":
        message = input("envoyé:")
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()
        print(data)

    client_socket.close()

if __name__ == '__main__':
    sys.exit(Client())