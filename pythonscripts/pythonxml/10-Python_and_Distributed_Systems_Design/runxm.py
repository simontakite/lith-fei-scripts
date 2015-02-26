"""
runxm.py - run xml message object
"""
import XMLMessage
from xml.dom.ext import PrettyPrint
#from xml.dom.ext.reader.Sax2 import FromXml

xm = XMLMessage.XMLMessage()

xm.loadXMLMessage("message.xml")

PrettyPrint(xm.getXMLMessageDom())

print "Change the body to: <body>Hello!</body>"
if xm.setBody("<body>Hello!</body>"):
  print xm.getXMLMessage()
