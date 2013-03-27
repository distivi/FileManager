#!/bin/python
import socket
import sys
import threading
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 21570

def serverAnswears():
	while 1:
		try:
			data = s.recv(1000000)
			if not data: sys.exit(0)
			print('received: ',data,'\nBytes: ',len(data))
		finally:
			pass

def sendMessagesToServer(socket_):	
	msg = input("Input your message: ")	
	s.send(bytes(msg,"utf-8"))
	
try:
	s.connect((host, port))
	print("Client Connected to server")
	
	inputT = threading.Thread(target=serverAnswears)
	inputT.daemon = True
	inputT.start()

	
	while True:
		sendMessagesToServer(s)

except:
	print("can't connet to server")
