#!/usr/bin/env python
# art.py

import sys

from xml.sax  import make_parser
from handlers import ArticleHandler

ch = ArticleHandler()
saxparser = make_parser()

saxparser.setContentHandler(ch)
saxparser.parse(sys.stdin)

# Added in the section "Using the Additional Information":
#
if ch.isMatch:
  print "News Item!"
  print "Title:", ch.title
  print "Body:", ch.body
