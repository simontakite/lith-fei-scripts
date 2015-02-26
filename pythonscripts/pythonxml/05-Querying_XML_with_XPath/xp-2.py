#!/usr/local/bin/python

import sys

from xml.dom.ext.reader import PyExpat
from xml.xpath          import Compile
from xml.xpath.Context  import Context

reader = PyExpat.Reader()
dom = reader.fromStream(sys.stdin)

expression = Compile("ship/@name")
context = Context(dom.documentElement)
nodes = expression.evaluate(context)

print "Nodes: ", nodes
