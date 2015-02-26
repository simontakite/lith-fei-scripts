"""
 XMLSwitchHandler.py
"""
import sys
import BaseHTTPServer
import StringIO

from urllib                  import unquote_plus
from XMLMessage              import XMLMessage
from xml.dom.ext             import PrettyPrint
from xml.dom.ext.reader.Sax2 import FromXml

class XMLSwitchHandler(
    BaseHTTPServer.BaseHTTPRequestHandler):
  def do_GET(self):
    """
     do_GET processes HTTP GET requests on the
     server port.
    """
    # send generic HTML response
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()
    self.wfile.write("<html><body>")
    self.wfile.write("<font face=tahoma size=2>")
    self.wfile.write("<b>Hello from XMLSwitchHandler!</b>")
    self.wfile.write("</font></body></html>")

  def do_POST(self):
    """
     do_POST processes HTTP POST requests and XML
     packets.
    """
    if self.headers.dict.has_key("content-length"):
      #
      # convert content-length from string to int
      content_length = int(self.headers.dict["content-length"])

      # read in the correct number of bytes from the client
      # and process the data
      raw_post_data = self.rfile.read(content_length)
      self.processXMLMessagePost(raw_post_data)
      return 1

    else:
      #
      # bad post
      self.send_reponse(500)
      return 0

  def processXMLMessagePost(self, strPostData):
    """
      processXMLMessagePost(strXMLMessage) - this
      method creates an XMLMessage from the supplied
      data and looks up a mapping from XMLMapping.xml
      to determine what object and method pair to
      invoke.
    """
    # icreate message by unquoting post data
    xmsg = XMLMessage()
    xmsg.setXMLMessage(
      unquote_plus(strPostData).replace("n=", ""))

    # check header for <rpc/> element
    strHeader = xmsg.getHeader()
    if strHeader.rfind("<rpc/>") < 0:
      # send back an HTML echo resonse
      self.echoResponse(strPostData)
      return 0

    # eval out object.method(params)
    msgDom     = xmsg.getXMLMessageDom()
    objElem    = msgDom.getElementsByTagName("object")[0]
    object     = objElem.getAttributeNS('',"class")
    method     = objElem.getAttributeNS('',"method")
    params     = []
    paramElems = msgDom.getElementsByTagName("param")

    # Get parameters as strings
    for thisparam in paramElems:
      strParam = StringIO.StringIO()
      PrettyPrint(thisparam, strParam)
      parameter = strParam.getvalue().strip()
      parameter = parameter.replace("<param>", "")
      parameter = parameter.replace("</param>", "")
      params.append(parameter)

    # instantiate correct object
    if object == "CustomerProfile":
        from CustomerProfile import CustomerProfile
        inst = CustomerProfile()

    if object == "XMLOffer":
        from XMLOffer import XMLOffer
        inst = XMLOffer()

    # '''''''''''''''''''''''''''''''''''''''''
    # add additional object instantiations here
    # '''''''''''''''''''''''''''''''''''''''''

    # prepare cmd string
    cmd = "inst." + method + "("

    # add parameters to command if necessary, separated
    # by """ and commas
    if len(params) == 1:
        cmd += "\"\"\"" + params[0] + "\"\"\"" + ")"
    elif(len(params) > 1):
      for pmIndex in range(0, (len(params) - 1)):
        cmd += "\"\"\"" + params[pmIndex] + "\"\"\"" + ", "
      cmd += "\"\"\"" + params[len(params)-1] + "\"\"\")"

    # if no params, just close off parens: ()
    if not params:
        cmd += ")"

    # execute cmd and capture result
    rezult = eval(cmd)

    # build response XML
    returnDom = FromXml(
      "<message>\n\t<header>\n\t\t<rpc-response/>\n\t</header>\n" +
      "\t<body>\n\t\t<object class=\"" + str(object) + "\" method=\"" +
      str(method) + "\">\n\n\t\t\t<response>" + str(rezult) +
      "</response>\n\t\t</object>\n\t</body>\n</message>\n")

    # optional hook: validate against return dom or
    #           any other special logic

    # prepare string of document element
    # (cut out prolog for xml message)
    strReturnXml = StringIO.StringIO()
    PrettyPrint(returnDom.documentElement, strReturnXml)
    xmlval = strReturnXml.getvalue()

    # return XML over HTTP to caller
    self.send_response(200)
    self.send_header("Content-type", "text/xml")
    self.send_header("Content-length", str(len(xmlval)))
    self.end_headers()
    self.wfile.write(str(xmlval))

    return 1

  def echoResponse(self, strPostData):
    """
      echoResponse(postData) - returns the post data
      parsed into a header and body chunk.
    """
    # send response
    self.send_response(200)
    self.send_header("Content-type", "text/html")
    self.end_headers()

    # send HTML text
    self.wfile.write("<html><body>"
                     "<font color=blue face=tahoma size=5>"
                     "<b>Hello from XMLSwitchHandler!</b></font><br><br>"
                     "<font face=arial,verdana,helvetica size=4>"
                     "Attempting to create XML Message "
                     "from source...<br><br>Header:<br><xmp>")

    msg = XMLMessage()
    msg.setXMLMessage(unquote_plus(strPostData).replace("n=", ""))

    # parse message into header and body, display as
    # example on web page
    self.wfile.write(msg.getHeader())
    self.wfile.write("</xmp></font><font face=arial,verdana,helvetica"
                     " size='4'>Body:<br><xmp>")

    self.wfile.write(msg.getBody())
    self.wfile.write("</xmp></font></body></html>")
