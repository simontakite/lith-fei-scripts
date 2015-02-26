#!/usr/bin/env python
#
# generates HTML from pyxml.xml

import sys

from xml.sax  import make_parser
from handlers import PyXMLConversionHandler

dh = PyXMLConversionHandler(sys.stdout)
parser = make_parser()

parser.setContentHandler(dh)
parser.parse(sys.stdin)
