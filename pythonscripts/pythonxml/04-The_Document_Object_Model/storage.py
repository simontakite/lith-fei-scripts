# storage.py
from article import Article

class Storage:
  """Stores and retrieves article objects as XML file
  --- should be easy to migrate to a database."""

  def save(self, article):
    """Save as <article.title>.xml."""
    sFilename = article.title + ".xml"
    fd = open(sFilename, "w")

    # write file to disk with data from getXML() call
    fd.write(article.getXML())
    fd.close()

  def load(self, sName):
    """Name must be filename.xml--Returns an article object."""
    fd = open(sName, "r")
    sxml = fd.read()

    # create an article instance
    a = Article()

    # use fromXML to initialize the article object
    # from the file's XML
    a.fromXML(sxml)
    fd.close()

    # return article object to caller
    return a
