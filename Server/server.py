# -*- coding: utf-8 -*-
#!/bin/python
import asyncore
import socket
import os
import sys
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import string
import re
import pickle

class MainServerSocket(asyncore.dispatcher):
  def __init__(self, port):
    asyncore.dispatcher.__init__(self)    
    self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'    
    try:      
      self.bind((host,port))      
      print("Socket binded")
      self.listen(1000)
    except:
      print("can't bind to socket ",host,':',port)
      sys.exit(0)     

  def handle_accept(self):
    newSocket, address = self.accept()
    print("Connected from",address)
    SecondaryServerSocket(newSocket)


class SecondaryServerSocket(asyncore.dispatcher_with_send):
  def handle_read(self):
    receivedData = self.recv(1024**2)
    if receivedData:
      print(receivedData)
      if len(receivedData) < 10:
        self.sendXML()
      else:
        self.sendPhotos()  
    else:
      self.close()

  def sendXML(self):
    xmlString = "<root><name>ololo</name></root>"
    self.send(pickle.dumps(xmlString))
 

  def sendPhotos(self): 
    dict1 = {"name1":"image1","name2":"image2"}
    image = open("./resources/4.jpg",'rb')    
    data = image.read()
    print(data)
    image.close()
    dict1["bytes_image"] = data
    self.send(pickle.dumps(dict1))
    pass

  def handle_close(self):
    print("Disconnected from: ",self.getpeername())  



if __name__ == '__main__':
  if len(sys.argv) < 2:
    print("You must write port for socket. For example: \"$ python server.py 7000\"")
    sys.exit(1)
  else:    
    if re.match('^[0-9]+$',sys.argv[1]):
      MainServerSocket(int(sys.argv[1]))
      asyncore.loop()
    else:
      print("Socket port must be a number")  


