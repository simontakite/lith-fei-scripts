"""
 XMLMessage.py - a wrapper for message.xml
 documents
"""
import StringIO

from xml.dom.ext             import PrettyPrint
from xml.dom.ext.reader.Sax2 import FromXmlStream, FromXml

class XMLMessage:
  """
   XMLMessage encapsulates a message.xml document
   from class users.
  """
  def __init__(self):
    self._dom = ""
    self._xml = ""

  def setBody(self, strXML):
    """
     setBody(strXML) - The supplied XML
     is used for the body of the XML message.
    """
    xmlstr = FromXml(str("<message>" +
                         self._header + strXML + "</message>"))
    return self.setXMLMessageDom(xmlstr)

  def getBody(self):
    """ return body as string
    """
    return self._body

  def setHeader(self, strXML):
    """
     setHeader(strXML) - The supplied XML
     is used for the header of the XML message.
    """
    xmlstr = FromXml(str("<message>" + strXML + self._body + "</message>"))
    return self.setXMLMessageDom(xmlstr)

  def getHeader(self):
    """ return header as string
    """
    return self._header

  def setXMLMessage(self, strXMLMessage, dom=0):
    """
     setXMLMessage - uses supplied XML as entire
     XML message
    """
    try:
      if dom:
        # assign dom directly with parameter
        self._dom = strXMLMessage

        # populate StringIO object for self._xml
        Holder = StringIO.StringIO()
        PrettyPrint(self._dom, Holder)

        # assign string value of dom to self._xml
        self._xml = Holder.getvalue()
      else:
        # create dom from supplied string XML
        dom = FromXml(strXMLMessage)

        # set member dom property
        self._dom = dom

        # set member string property
        self._xml = strXMLMessage

      # header as DOM
      self._headerdom = self._dom.getElementsByTagName("header")[0]

      # header as string
      Holder = StringIO.StringIO()
      PrettyPrint(self._dom.getElementsByTagName("header")[0],
                  Holder)
      self._header = Holder.getvalue()

      # body as DOM
      self._bodydom = self._dom.getElementsByTagName("body")[0]

      # body as string
      Holder = StringIO.StringIO()
      PrettyPrint(self._dom.getElementsByTagName("body")[0],
                  Holder)
      self._body = Holder.getvalue()


    except:
      print "Could not create dom from message!"
      return 0

    return 1

  def setXMLMessageDom(self, xmldom):
    """ call setXMLMessage with dom flag
    """
    return self.setXMLMessage(xmldom, dom=1)

  def loadXMLMessage(self, file):
    """
     loadXMLMessage - build an XML message from
     a file or URL
    """
    try:
      dom = FromXmlStream(file)
    except:
      print "Could not load XML Message."
      return 0

    return self.setXMLMessageDom(dom)

  def getXMLMessage(self, dom=0):
    """
     getXMLMessage - returns the entire message
     as either string of XML or Dom
    """
    if dom:
      return self._dom
    else:
      return self._xml


  def getXMLMessageDom(self):
    """ return XML message dom property
    """
    return self.getXMLMessage(dom=1)
