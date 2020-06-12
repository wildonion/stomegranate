 # coding: utf-8
'''
	Designed By : 
 █     █░ ██▓ ██▓    ▓█████▄  ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▓█░ █ ░█░▓██▒▓██▒    ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒█░ █ ░█ ▒██▒▒██░    ░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
░█░ █ ░█ ░██░▒██░    ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░░██▒██▓ ░██░░██████▒░▒████▓ ░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██
		by cL34n 3v3RytH!n9
'''
# python http webserver using http module(watch?v=hFNZ6kdBgO0) or socket module(watch?v=_najJkyK46g) or flask module(watch?v=vyCboBjK4us) or watch?v=2KeSfeIo2MI

# TODO: make a UI to work with it on terminal like msf, setoolkit,.. to control the whole attack after spreading the virus 
# TODO: More secure socket connection using SSL => create ur server like Orcus in order to untrackble : https://docs.python.org/2/library/ssl.html
# TODO: ctrl + C to cancel the server  

#!/usr/bin/python 
# forward port 3389 for RDP over WAN or setup a reverse proxy on vic machine to bypass firewall

import os, time, socket, argparse, errno
from socket import error as socket_error

class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

def cRy():
	parser = argparse.ArgumentParser()
	parser.add_argument("--host", help="Host To Listen")
	parser.add_argument("--port", help="Port To Listen", type=int)
	args = parser.parse_args()

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((args.host, args.port))
	s.listen(1)
	print bcolors.OKGREEN + "[+] Onion is R3adY 2 cRy..."

	try:
		conn, addr = s.accept() # target can connect from his/her terminal(client.exe or client.py) or browser(with a link) and this is how msf http(s) reverse shell works and u can hack with just a link!!
		time.sleep(1)
		print "[+] V1cT1m-IP => {}".format(addr[0]) + bcolors.ENDC
		conn.close()
	except socket_error as serr:
		if serr.errno != errno.ECONNREFUSED:
			raise serr
	except KeyboardInterrupt:
		print "[-] k3y pr3ss3d"


if __name__ == "__main__":
	cRy()

