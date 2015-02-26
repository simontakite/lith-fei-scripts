#!/usr/bin/env python

from xml.dom.ext.reader.Sax2 import FromXmlStream
import sys

def findTextNodes(nodeList):
  for subnode in nodeList:
    if subnode.nodeType == subnode.ELEMENT_NODE:
      print "element node: " + subnode.tagName

      # call function again to get children
      findTextNodes(subnode.childNodes)

    elif subnode.nodeType == subnode.TEXT_NODE:
      print "text node: ",
      print subnode.data

doc = FromXmlStream(sys.stdin)
findTextNodes(doc.childNodes)
