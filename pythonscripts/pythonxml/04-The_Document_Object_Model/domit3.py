#!/usr/local/bin/python
# domit.py

from xml.dom.ext.reader.Sax2 import FromXmlStream
from xml.dom.ext             import PrettyPrint
from xml.dom                 import DOMImplementation

import sys

def makeSize(nodeList):
  for subnode in nodeList:
    if (subnode.nodeType == subnode.ELEMENT_NODE):
      makeSize(subnode.childNodes)
    if (subnode.nodeName == "size"):
      subnode.parentNode.parentNode.replaceChild(subnode, subnode.parentNode)

#
# get DOM object
doc = FromXmlStream(sys.stdin)

#
# call func
makeSize(doc.childNodes)

#
# display altered document
PrettyPrint(doc)





