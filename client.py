from socket import *
import socket
import sys

SERVER_HOST = 'localhost'
SERVER_PORT = 15322
ADDR = (SERVER_HOST, SERVER_PORT)
BUFF_SIZE = 1024

if __name__ == "__main__":
    try:
        client_socket = socket.socket(AF_INET, SOCK_STREAM, 0)
    except socket.error as err:
        print("Failed to create socket because", err)
        sys.exit()

    client_socket.connect(ADDR)
    while True:
        mess = input("Client: ")
        client_socket.send(mess.encode('utf-8'))
        if mess == "end":
            print("End call")
            client_socket.close()
        else:
            mess = client_socket.recv(BUFF_SIZE)
            print("Server: ", mess.decode('utf-8'))
