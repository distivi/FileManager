import socket
import select
import sys

servsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servsock.bind(("", 2500))
servsock.listen(15)
servsock.setblocking(1)

readlist = [servsock]

while 1:
	(sread, swrite, sexc) =  select.select(readlist, [], [] ); 

	for sock in sread:
		#received a connect to the server socket
		if  sock == servsock:
			newsock, address = servsock.accept()
			#newsock.setblocking(1)
			print("I got a connection from ", address)
			readlist.append(newsock)
			newsock.send(bytes("you're connected to the select server","utf-8"))
