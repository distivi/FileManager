import sys
import os
import re
from socket import *
from threading import *
import pickle

HOST = '127.0.0.1'
BUFSIZE = 1024**2*10 # 10 Mb

class Client:	
	def __init__(self, port):		
		self.tcpSock = socket(AF_INET, SOCK_STREAM)
		try:
			self.tcpSock.connect((HOST, port))
			print("Connetcted to server")
		except:
			print("connection failed")
			sys.exit(0)

	def run(self):
		self.serverCallBack()
		self.userMenu()
		

	def serverCallBack(self):
		def loop0():
			while True:
				data = self.tcpSock.recv(BUFSIZE)
				if data: 
					#print(data)
					print(pickle.loads(data))
				else:
					print("Connection lost")
					sys.exit(0)

		t = Thread(target=loop0)		
		t.daemon = True
		t.start()

		
	def userMenu(self):
		while True:
			command = input(">>>")
			self.tcpSock.send(bytes(command,'utf-8'))

if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("You must write port for socket. For example: \"$ python client.py 7000\"")
		sys.exit(1)
	else:    
		if re.match('^[0-9]+$',sys.argv[1]):
			client = Client(int(sys.argv[1]))		
			client.run()
		else:
			print("Socket port must be a number")  
		


