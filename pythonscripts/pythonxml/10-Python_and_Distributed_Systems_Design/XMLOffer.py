"""
XMLOffer.py
"""
import StringIO

from xml.dom.ext.reader.Sax2 import FromXmlStream
from xml.dom.ext.reader.Sax2 import FromXml
from xml.dom.ext             import PrettyPrint
from xml.xpath               import Evaluate

class XMLOffer:
  def getOffer(self, strId, dom=0):
    """
    getOffer takes an ID as a parameter and returns
    the corresponding offer from the XML Data Store
    as a string of XML, or as a DOM if the third param
    flag has been set.
    """
    # create document from data store
    offerdoc = FromXmlStream("OfferXMLStore.xml")

    # use XPath to target specific offer element
    # by child ID character data
    offer = Evaluate("offer[id='" + strId + "']",
                     offerdoc.documentElement)

    # decide which version to return, dom or string
    if dom:
        # return offer element
        return offer[0]
    else:
        # convert to string
        strXML = StringIO.StringIO()
        PrettyPrint(offer[0], strXML)
        return strXML.getvalue()

  def getOfferAsDomElement(self, strId):
    """
    getOfferAsDomElement works the same as getOffer
    but returns a DOM element instance, as opposed to
    a string.  This method just call getOffer with the
    dom flag (the third parameter) set to 1.
    """
    return self.getOffer(strId, 1)

  def getAllOffers(self):
    """
    getAllOffers returns the whole store
    as a string.
    """
    # scoop up offers file
    fd = open("OfferXMLStore.xml", "r")
    doc = fd.read()
    fd.close()

    # return big string
    return doc

  def insertOffer(self, strOfferXML):
    """
    insertOffer takes a string of XML and adds it to the
    XML store.
    """
    if not strOfferXML:
        return None

    # generate DOM from input data
    newoffer = FromXml(strOfferXML)

    #----
    # optional: you could validate here using
    # your new dom object and offer.dtd, see
    # chapter 7 for details on using xmlproc for
    # validation...
    #----

    # Pour DOM into String
    newXmlOffer = StringIO.StringIO()
    PrettyPrint(newoffer.documentElement, newXmlOffer)

    # grab contents into buffer
    rd = open("OfferXMLStore.xml", "r")
    bf = rd.readlines()
    rd.close()

    # search and replace in buffer
    wd = open("OfferXMLStore.xml", "w")
    for lp in range(len(bf)):
        if (bf[lp].rfind("</OfferXMLStore>") > -1):
            # replace root element end tag with fresh offer
            # and root element end tag
            bf[lp] = bf[lp].replace("</OfferXMLStore>",
              newXmlOffer.getvalue() + "</OfferXMLStore>")

    # write new buffer to disk
    wd.writelines(bf)
    wd.close()

    return 1

  def deleteOffer(self, strId):
    """
    deleteOffer takes an ID string and
    deletes that offer Node out of the
    OfferXMLStore.xml document
    """
    # read store into DOM, close store
    try:
      xmlstore = FromXmlStream("OfferXMLStore.xml")
    except:
      print "Unable to open xmlstore."
      return 0

    # use XPath to return the id Node
    # offer/[id='<id>']
    try:
      targetNode = Evaluate("offer[id=\"" + strId + "\"]",
                            xmlstore.documentElement)
    except:
      print "Bad XPath Evaluation."
      return 0

    # use Node.removeChild(XPathResult)
    try:
      xmlstore.documentElement.removeChild(targetNode[0])
    except:
      # either it didn't exist, or
      # the XPath call turned up nothing...
      return 0

    # reopen store,w
    # PrettyPrint the DOM in
    # close the store
    fd = open("OfferXMLStore.xml", "w")
    PrettyPrint(xmlstore, fd)
    fd.close()
    return 1

  def updateOffer(self, strOfferXML):
    if not strOfferXML:
      return 0
    else:
      try:
        offerId = Evaluate("id/text()",
                           FromXml(strOfferXML).documentElement)
        if (not self.deleteOffer(offerId[0].nodeValue)
            or not self.insertOffer(strOfferXML)):
          print "could not delete or insert."
          return 0
      except:
        print "unable to update offer."
        return 0

    return 1
