

# https://null-byte.wonderhowto.com/how-to/hacking-windows-10-find-sensitive-deleted-files-remotely-0183748/
# u can use post-exploitation module in msf to recover files; just see above link

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

import socket 
import os

host = '127.0.0.1'
port = 8234

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind((host, port))
serversock.listen(5)
print '[+] Server Listening On Port : ', port

conn, addr = serversock.accept()
print '[+] Connection Has Been Stablished By => ', addr