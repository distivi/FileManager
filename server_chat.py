#!/bin/python
import asyncore
import socket

clients = {}

class MainServerSocket(asyncore.dispatcher):
	def __init__(self, port):
		asyncore.dispatcher.__init__(self)
		self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
		self.bind(('',port))
		self.listen(5)
	def handle_accept(self):
		newSocket, address = self.accept( )
		clients[address] = newSocket
		print("Connected from", address)
		SecondaryServerSocket(newSocket)

class SecondaryServerSocket(asyncore.dispatcher_with_send):
	def handle_read(self):
		receivedData = self.recv(1000000)
		if receivedData:
			every = clients.values()
			print(receivedData)				
			receivedMsg = receivedData.decode("utf-8")
			print(receivedMsg)
			msg = receivedMsg + "\n"
			print(msg)
			for one in every:
				one.send(bytes(msg,'utf-8'))
		else: self.close( )
		
	def handle_close(self):
		print("Disconnected from", self.getpeername( ))
		one = self.getpeername( )
		del clients[one]

MainServerSocket(21570)
asyncore.loop( )