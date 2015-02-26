import xml.dom.minidom
from xml.sax.saxutils import escape

class Article:
  """Represents a block of text and metadata created from XML."""

  def __init__(self):
    """Set initial data properties."""
    self.reset()

  def reset(self):
    """Re-initialize data properties."""
    self.title       = ""
    self.size        = 0
    self.time        = ""    # pretty-printing time string
    self.author      = ""
    self.contributor = ""
    self.contents    = ""

  def getXML(self):
    """Returns XML after re-assembling from data
    members that may have changed."""

    attr = ''
    if self.title:
      attr = ' title="%s"' % escape(self.title)
    s = '<?xml version="1.0"?>\n<article%s>\n' % attr
    if self.author:
      s = '%s  <author name="%s" />\n' % (s, escape(self.author))
    if self.contributor:
      s = '%s  <contributor name="%s" />\n' % (s, escape(self.contributor))
    if self.contents:
      s = ('%s  <contents>\n%s\n  </contents>\n'
           % (s, escape(self.contents)))
    return s + "</article>\n"

  def fromXML(self, data):
    """Initialize using an XML document passed as a string."""
    self.reset()
    dom              = xml.dom.minidom.parseString(data)
    self.title       = get_attribute(dom, "article", "title")
    self.size        = int(get_attribute(dom, "size", "bytes") or 0)
    self.time        = get_attribute(dom, "time", "stime")
    self.author      = get_attribute(dom, "author", "name")
    self.contributor = get_attribute(dom, "contributor", "name")
    nodelist         = dom.getElementsByTagName("contents")
    if nodelist:
      assert len(nodelist) == 1
      contents = nodelist[0]
      contents.normalize()
      if contents.childNodes:
        self.contents = contents.firstChild.data.strip()

# Helper function:

def get_attribute(dom, tagname, attrname):
  """Return the value of a solitary element & attribute,
  if available."""
  nodelist = dom.getElementsByTagName(tagname)
  if nodelist:
    assert len(nodelist) == 1
    node = nodelist[0]
    return node.getAttribute(attrname).strip()
  else:
    return ""
