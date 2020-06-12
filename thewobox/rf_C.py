


import socket
import os

host = '18.216.53.253'
port = 13500

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.conncet((host, port))