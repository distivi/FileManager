#!/bin/python
# -*- coding: utf-8 -*-

import pickle
import re
import xml.etree.ElementTree as ET
from resources_manager import ResourcesManager

class Api:
	def __init__(self, delegate_ = None):
		self.delegate = delegate_
		self.resources_manager = ResourcesManager()

	def receiveData(self, data):
		print(data)	
		output_data = self.queryParser(data)

		send_fun = getattr(self.delegate, 'send_data')
		if send_fun:
			print(len(output_data))
			print('\n\n\n\n\n\n',output_data,'\n\n\n\n')
			send_fun(output_data)
			'''
			if (len(data) < 5):
				xmlData = self.resources_manager.getResourcesXMLData()
				print(output_data)
				#fun(xmlData)
			else:
				print("send images")
				fun(pickle.dumps(["123412","asdfasdf"]))
			'''

	def queryParser(self, data):	
		strQuery = data.decode()
		print(strQuery)	
		if re.match('^\s*[Hh]elp\s*$',strQuery):
			return self.help()
		elif re.match('^\s*files info\s*$',strQuery):
			return self.resources_manager.getResourcesXMLData()
		elif re.match('^(\s*\d+\s*,)+\s*\d+\s*',strQuery):
			return self.photosData(strQuery)
		else:
			return bytes("Wrong query, try type \"Help\"",'utf-8')
			

	def help(self):
		root = ET.Element('root')
		root.attrib = {'ID':'HELP'}			
		nodeGetFilesInfo = ET.SubElement(root,'help')
		nodeGetFilesInfo.text = "To get help info send string:\"help\""

		nodeGetFilesInfo = ET.SubElement(root,'files_info')
		nodeGetFilesInfo.text = "To get files info send string:\"files info\""
		
		nodeDownloadFiles = ET.SubElement(root,'download_files')
		nodeDownloadFiles.text = "To download files send file name's ot id's separated by commas:"
		
		xmlData = ET.tostring(root, encoding="utf-8")
		return xmlData


	def photosData(self,inputString):
		newstr = re.sub(',{1,}',',',inputString)		
		newstr = re.sub(' {1,}','',newstr)		
		fileIDs = re.split(',',newstr)
		print(fileIDs)
		return bytes('ololo','utf-8')
'''
		dict1 = {"name1":"image1","name2":"image2"}
		image = open("./resources/4.jpg",'rb')	
		data = image.read()
		print(data)
		image.close()
		dict1["bytes_image"] = data
		#self.send(pickle.dumps(dict1))
		
'''