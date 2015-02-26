#!/usr/bin/env python

from xml.dom.ext.reader.Sax2 import FromXmlStream
import sys

doc = FromXmlStream(sys.stdin)

for sku in doc.getElementsByTagName("sku"):
  sku.normalize()
  print "Sku: " + sku.firstChild.data
