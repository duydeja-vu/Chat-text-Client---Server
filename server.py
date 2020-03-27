from socket import *
import socket
import sys
import numpy as np


HOST = '127.0.0.1'
PORT = 15322
BUFF_SIZE = 1024
ADDR = (HOST, PORT)

if __name__ == "__main__":
    try:
        server_socket = socket.socket(AF_INET, SOCK_STREAM, 0)
    except socket.error as err:
        print("Failed to create socket because", err )
        sys.exit()

    print("Successfully for create socket, waiting for connection")
    server_socket.bind(ADDR)
    server_socket.listen(5)
    client_socket, client_addr = server_socket.accept()
    print("Conection with %s has been established" %str(client_addr))
    while True:
        mess = client_socket.recv(BUFF_SIZE)
        print("Client: ", mess.decode('utf-8'))
        if mess.decode('utf-8') == "end":
            print("End call")
            server_socket.close()
        else:
            mess = input("Server: ")
            client_socket.send(mess.encode('utf-8'))


    