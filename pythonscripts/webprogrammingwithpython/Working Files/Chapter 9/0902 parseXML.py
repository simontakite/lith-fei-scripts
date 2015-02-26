import xml.sax

class FilmParser(xml.sax.ContentHandler):
   def __init__(self):
      xml.sax.ContentHandler.__init__(self)

   def startElement(self, name, attrs):
      print("start element: '" + name + " ' ")