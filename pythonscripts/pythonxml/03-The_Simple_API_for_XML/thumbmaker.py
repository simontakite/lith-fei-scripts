#!/usr/bin/env python
# thumbmaker.py

import sys

from xml.sax   import make_parser
from saxthumbs import SAXThumbs

# Main

ch = SAXThumbs(sys.argv[1])
parser = make_parser()

parser.setContentHandler(fh)
parser.parse(sys.stdin)
