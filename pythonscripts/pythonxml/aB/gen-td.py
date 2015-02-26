"""Generate HTML for terms and definitinos
directly from XML specification.

XML source must come from standard input
"""
import sys

from xml.sax import ContentHandler
from xml.sax import make_parser


class XMLSpecHandler(ContentHandler):
    """
    Class implements part of SAX API to pull term
    definitions out of the XML Specification source file.
    """
    inTermDef = 0

    def startElement(self, name, attrs):
      if name == "termdef":
        self.inTermDef = 1
        self.strTermDefContents = ""
        print "<p><b>" + attrs.get('term', "") + "</b><br>"

    def characters(self, ch):
      if self.inTermDef:
        self.strTermDefContents += ch

    def endElement(self, name):
      if name == "termdef":
        self.inTermDef = 0
        self.strTermDefContents += "</p>"

        print self.strTermDefContents

# Main
if __name__ == "__main__":
  dh = XMLSpecHandler()
  parser = make_parser()
  parser.setContentHandler(dh)

  print "<html><body>"
  print "<style type='text/css'>"
  print "body { font-family: sans-serif; }"
  print "</style>"
  print "</head><body>"
  parser.parse(sys.stdin)
  print "</body></html>"
