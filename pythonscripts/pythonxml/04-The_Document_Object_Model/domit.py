#!/usr/bin/env python
import sys

from xml.dom.ext.reader.Sax2 import FromXmlStream
from xml.dom.ext             import PrettyPrint

# get DOM object
doc = FromXmlStream(sys.stdin)

# remove unwanted nodes by traversing Node tree

for node1 in doc.childNodes:
  for node2 in node1.childNodes:
    node2.normalize()
    node3 = node2.firstChild
    while node3 is not None:
      next = node3.nextSibling
      name = node3.nodeName
      if name in ("contents", "extension", "userID", "groupID"):
        # remove unwanted nodes here via the parent
        node2.removeChild(node3)
      node3 = next

PrettyPrint(doc)
