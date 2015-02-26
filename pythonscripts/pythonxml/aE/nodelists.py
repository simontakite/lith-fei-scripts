"""
 nodelists.py - using the NodeList object
  from MSXML3.0
"""
import win32com.client

# source XML
strSourceDoc = "people.xml"

# instantiate parser
objXML = win32com.client.Dispatch("MSXML2.DOMDocument.3.0")

# check for successful loading
if (not objXML.load(strSourceDoc)):
  print "Error loading", strSourceDoc

# grab all person elements
peopleNodes = objXML.getElementsByTagName("person")

# begin iteration of NodeList with nextNode()
node = peopleNodes.nextNode()
while node:
  # print value of text descendants
  print "Name: ", node.text,

  # print value of title attribute
  print "\tPosition: ", node.getAttribute("title")

  # continue iteration
  node = peopleNodes.nextNode()
