from xml.sax.handler import ContentHandler

class ArticleHandler(ContentHandler):
  """A handler to deal with articles in XML"""

  inArticle = 0
  inBody    = 0
  isMatch   = 0
  title     = ""
  body      = ""

  def startElement(self, name, attrs):
    if name == "webArticle":
      subcat = attrs.get("subcategory", "")
      if subcat.find("tech") > -1:
        self.inArticle = 1
        self.isMatch = 1

    elif self.inArticle:
      if name == "header":
        self.title = attrs.get("title", "")
      if name == "body":
        self.inBody = 1

  def characters(self, characters):
    if self.inBody:
      if len(self.body) < 80:
        self.body += characters
      if len(self.body) > 80:
        self.body = self.body[:78] + "..."
        self.inBody = 0

  def endElement(self, name):
    if name == "body":
      self.inBody = 0


class PyXMLConversionHandler(ContentHandler):
  """A simple handler implementing 3 methods of
  the SAX interface."""

  def __init__(self, fp):
    """Save the file object that we generate HTML into."""
    self.fp = fp

  def startDocument(self):
    """Write out the start of the HTML document."""
    self.fp.write("<html><body><b>\n")

  def startElement(self, name, attrs):
    if name == "file":
      # generate start of HTML
      s = attrs.get('name', "")
      self.fp.write("<p>File: %s<br>\n" % s)

    elif name == "class":
      self.fp.write("&nbsp;" * 3 + "Class: "
                    + attrs.get('name', "") + "<br>\n")

    elif name == "method":
      self.fp.write("&nbsp;" * 6 + "Method: "
                    + attrs.get('name', "") + "<br>\n")

  def endDocument(self):
    """End the HTML document we're generating."""
    self.fp.write("</b></body></html>")
