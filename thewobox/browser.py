
# socket python browser
# TODO : we can access to cookie on client side then why we just don't put some virus or backdoor in user cookie so everythime he/she try to load our site our virus run itself from cookie! our encoded jwt has some virus code(js/python/bytecode) with expiration date so when our user try to login this code will sign and we send its token along with the secret key to the client then on a specific time this token will decrypt.

import socket
import sys  

host = sys.argv[1]
port = 80  # web

# create socket
print('[+] Creating socket')
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('[-] Failed to create socket')
    sys.exit()

print('[+] Getting remote IP address') 
try:
    remote_ip = socket.gethostbyname( host )
except socket.gaierror:
    print('[-] Hostname could not be resolved. Exiting')
    sys.exit()

# Connect to remote server
print('[+] Connecting to server, ' + host + ' (' + remote_ip + ')')
s.connect((remote_ip , port))

# Send data to remote server
print('[+] Sending data to server')
request = "GET / HTTP/1.0\r\n\r\n"

try:
    s.sendall(request)
except socket.error:
    print '[-] Send failed'
    sys.exit()

# Receive data
print('[+] Receive data from server')
reply = s.recv(4096)

print reply 
