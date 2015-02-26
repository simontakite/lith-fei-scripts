#!/usr/bin/env python

from xml.dom.ext.reader.Sax2 import FromXmlStream
from xml.dom.ext             import PrettyPrint

import sys

def makeSize(nodeList):
  for subnode in nodeList:
    if subnode.nodeType == subnode.ELEMENT_NODE:
      if subnode.nodeName == "size":
        subnode.parentNode.parentNode.replaceChild(
          subnode, subnode.parentNode)
      else:
        makeSize(subnode.childNodes)

# get DOM object
doc = FromXmlStream(sys.stdin)

# call func
makeSize(doc.childNodes)

# display altered document
PrettyPrint(doc)
