"""
genhtml2.py - generates HTML from pyxml.xml
"""

import sys

from xml.parsers import expat
from handlers    import PyXMLConversionHandler

dh = PyXMLConversionHandler(sys.stdout)
parser = expat.ParserCreate()

parser.StartElementHandler = dh.startElement
parser.EndElementHandler = dh.endElement
parser.CharacterDataHandler = dh.characters
parser.ParseFile(sys.stdin)
