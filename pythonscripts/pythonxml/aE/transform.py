"""
 transform.py - using MSXML3.0
 XSLT support from Python
"""
import win32com.client

strSourceDoc = "1999temps.xml"
strStyleDoc  = "temps.xsl"

objXML = win32com.client.Dispatch("MSXML2.DOMDocument.3.0")
objXSL = win32com.client.Dispatch("MSXML2.DOMDocument.3.0")

if (not objXML.load(strSourceDoc)):
  print "Error loading", strSourceDoc

if (not objXSL.load(strStyleDoc)):
  print "Error loading", strStyleDoc

strTransformedXML = objXML.transformNode(objXSL)
print strTransformedXML
