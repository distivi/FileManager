import sys
import os
import re
import time
from socket import *
from threading import *
import xml.etree.ElementTree as ET

HOST = '127.0.0.1'
BUFFSIZE = 1024**2*30 # 10 Mb

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
				self.tcpSock.setblocking(0)
				timeout = 1
				total_data = []
				start_time = time.time()
								
				while True:										
					if total_data and time.time() - start_time > timeout:						
						break
					elif time.time() - start_time > timeout * 2:											
						break

					try:
						data = self.tcpSock.recv(BUFFSIZE)						
						if data:
							total_data.append(data)							
							start_time = time.time()							
						else:
							print("Connection lost")
							self.tcpSock.close()
							sys.exit(0)
					except:
						pass
				
				if total_data:					
					total_data = b''.join(total_data)
					self.parseData(total_data)
					print('\n>>>', end="")

		t = Thread(target=loop0)		
		t.daemon = True
		t.start()

	def parseData(self,data):		
		strData = data.decode()
		print("input string: ",strData)		
		try:
			root = ET.fromstring(strData)
			print(root.attrib['ID'])			
			if root.attrib['ID'] == 'HELP':
				self.parseHelpXML(root)
			elif root.attrib['ID'] == 'FILES_INFO':
				self.parseFilesInfo(root)
			
		except:
			print("obtained something else, may be a picture")

	def parseHelpXML(self, root):
		print('_'*90)
		for child in root:
			print('| ',child.tag.ljust(15),'| ',child.text.ljust(68),'|')
		print('-'*90)

	def parseFilesInfo(self, root):
		#print('| ID |',' file name'.ljust(30))
		print('|',end="")		
		print('{:_^7}'.format('ID'),end="")
		print('|',end="")
		print('{:_^50}'.format('file name'),end="")
		print('|',end="")
		print('{:_^30}'.format('description'),end="")
		print('|')		
		for fileNode in root:
			print('|',fileNode[0].text.ljust(5),'|',end="")
			print(fileNode[1].text.ljust(50),'|',end="")
			print(fileNode[3].text.ljust(30),'|')
		print('-'*95)


		
	def userMenu(self):
		print('\n>>>', end="")
		while True:
			command = input()
			if command == 'exit':
				self.tcpSock.close()
				sys.exit(0)
			else:
				self.tcpSock.send(bytes(command,'utf-8'))

if __name__ == '__main__':
	if len(sys.argv) < 2:
		#print("You must write port for socket. For example: \"$ python client.py 7000\"")
		sys.exit(1)
	else:    
		if re.match('^[0-9]+$',sys.argv[1]):
			client = Client(int(sys.argv[1]))		
			client.run()
		else:
			print("Socket port must be a number")  
		


