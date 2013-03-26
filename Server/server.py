# -*- coding: utf-8 -*-
import os
#import xmp_parser
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
import string


class Server(object):
  # Singleton
  #_instance = None
  #def __new__(self, *args, **kwargs):       
    #if not self._instance:
      #self._instance = super(Server, self).__new__(self)
    #return self._instance
#
  resourcesDirName = None
   
  def __init__(self,arg = None):
    super(Server,self).__init__()

    self.resourcesDirName = "resources2"
    resourcesPath = os.path.join(os.getcwd(),self.resourcesDirName)
    
    if not os.path.isdir(resourcesPath):      
      os.makedirs(resourcesPath)

  def getXMLFile(self):    
    root = Element('root')
    files = self.getFilesFromResources()
    i = 0
    for tmpFile in files:
      nodeFile = SubElement(root,'file')
      
      nodeFileId = SubElement(nodeFile,'id')
      nodeFileId.text = str(i)

      nodeFileName = SubElement(nodeFile,'name')
      nodeFileName.text = tmpFile.split('/')[-1]

      nodeFilePath = SubElement(nodeFile,'path')
      nodeFilePath.text = tmpFile

      nodeFilePath = SubElement(nodeFile,'description')
      nodeFilePath.text = "default description"
      i += 1

    xmlFileName = self.resourcesDirName + '.xml'
    

    print(xmlFile)

    

  def getFilesFromResources(self):
    resourcesPath = os.path.join(os.getcwd(),self.resourcesDirName)
    resources = []
    for r,d,f in os.walk(resourcesPath):
      for files in f:
        resources.append(os.path.join(r,files))
    return resources


if __name__ == '__main__':
  init_dict = {"ip":"127.0.0.1"}
  s = Server(init_dict)
  s.getXMLFile()
  

  


#for r,d,f in os.walk("./resources"):
   # for files in f:
    	#print files
    #	print os.path.join(r,files)
        #if files.endswith(".txt"):
          #   print os.path.join(r,files)

