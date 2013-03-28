#!/bin/python
# -*- coding: utf-8 -*-

import os
import xml.etree.ElementTree as ET

class ResourcesManager(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			# craete singleton
			cls.instance = super(ResourcesManager, cls).__new__(cls)
		return cls.instance

	def __init__(self,resourcesDirName_ = 'resources', resourcesXML_ = 'resourcesXML.xml'):
		self.resourcesDirName = resourcesDirName_
		self.resourcesXML = resourcesXML_
		self.resourcesPath = os.path.join(os.getcwd(),self.resourcesDirName)
		if not os.path.isdir(self.resourcesPath):
			os.makedirs(self.resourcesPath)

	def getResourcesXMLData(self):
		print("getResourcesXMLData")		
		xmlData = None			
		if os.path.exists(os.path.join(os.getcwd(),self.resourcesXML)):
			xmlFile = open(self.resourcesXML,'rb')
			xmlData = xmlFile.read()
			xmlFile.close()
		else:
			root = ET.Element('root')		
			root.attrib = {'ID':'FILES_INFO'}	
			files = self.getFilesFromResources()
			i = 0
			for tmpFile in files:
				nodeFile = ET.SubElement(root,'file')
				
				nodeFileId = ET.SubElement(nodeFile,'id')
				nodeFileId.text = str(i)

				nodeFileName = ET.SubElement(nodeFile,'name')
				nodeFileName.text = tmpFile.split('/')[-1]

				nodeFilePath = ET.SubElement(nodeFile,'path')
				nodeFilePath.text = tmpFile

				nodeFilePath = ET.SubElement(nodeFile,'description')
				nodeFilePath.text = "default description"
				i += 1

			xmlData = ET.tostring(root, encoding="utf-8")

			xmlFile = open(self.resourcesXML,'wb')
			xmlFile.write(xmlData)
			xmlFile.close()

		return xmlData

	def getFilesFromResources(self):		
		resources = []
		for r,d,f in os.walk(self.resourcesPath):
			for files in f:
				resources.append(os.path.join(r,files))
		return resources

if __name__ == '__main__':
	rm = ResourcesManager()
	xmlstr = rm.getResourcesXMLData()
	print(xmlstr)
	pass