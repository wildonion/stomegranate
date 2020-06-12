
# a chatapp with UI over LAN using LAN cable to communicate with other pc in a same network
# turn it into a real world app to use it over WAN using pyp2p and crypto lib
# use cryptully and neuron scripts to complete this project 
# build my own messenger like telegram(build its cli also) use p2p or client/server model with a new cryptography protocol like telegram MTproto

'''
SOURCES:
http://telepot.readthedocs.io/en/latest/reference.html#telepot.Bot.getChatAdministrators => inspiration for ur bot api like telegram bot for ur SCA
http://www.cse.wustl.edu/~jain/cse571-07/ftp/p2p/
https://null-byte.wonderhowto.com/how-to/sploit-build-peer-peer-chat-application-python-gui-linux-0163617/
https://www.ynonperek.com/2018/01/18/writing-a-secure-encrypted-chat-in-python/
https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170
https://www.computerworld.com/article/2588254/networking/p2p-over-the-internet.html
'''

'''
Socket is used to transport data between systems. It simply connects two systems together, an IP address is the address of the machine over an IP based network.
With socket connection you can design your own protocol for network connection between two systems.
With Socket connection you need to take care of all the lower-level details of a TCP/IP connection.
'''

'''
TODO:
build smt like those chatroom which is in darknet like MRX chatroom in who am i movie
build a private chat like telegram
build ur own IRC client server model
python http(s)[ssl libs & make ur own certificate] & tcp server[socket lib] with download/upload feature
build a webserver with raspi & python like nginx and http apache
build a python http server => blog.wachowicz.eu/?p=256
use AES or RSA in ur algo and server
More secure socket connection using SSL
'''

import socket
import time

def Main():
	host = '127.0.0.1'
	port = 5001

	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	conn, addr = s.accept()
	print("[*] connection from: " + str(addr))
	while True:
		data = conn.recv(1024).decode()
		if not dat:
			break
		print("[*] from connected user: " + str(data))
		data = str(data).upper()
		print("[*] received from user: " + str(data))

		data = input(" ? ")
		conn.send(data.encode())
		conn.close()

if __name__ == '__main__':
	Main()