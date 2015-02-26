"""
  xsc.py - XMLSwitch Client

  usage:
    python xsc.py myRequestFile.xml

"""
import sys
import httplib
from urllib import quote_plus

class xsc:
  """
   xsc - XMLSwitch Client
   This class is both the command line and module
   interface to the XMLSwitch.

   From the cmd line:
   $> python xsc.py msgFile.xml

   The third parameter is an XML file with a valid
   <message> within it.  The response <message> will
   be written back to the console.

   As an API:
   import xsc
   responseXML = xsc.sendMessage(strXMLMessage)

   The result is now in responseXML.
  """
  def __init__(self):
    """
     init - establish some public props
    """
    self.server = "localhost:2112" # host:port (80 is http)
    self.stats  = ""

  def sendMessage(self, strXMLMessage):
    """
     sendMessage(strXML) - this method sends the
     supplied XML message to the server in self.server.
     The XML response is returned to the caller.
    """
    # prepare XML message by url encoding...
    strXMLRequest = quote_plus(strXMLMessage)

    # connect with server...
    req = httplib.HTTP(self.server)

    # add HTTP headers, including content-length
    # as size of our XML message
    req.putrequest("POST", "/")
    req.putheader("Accept", "text/html")
    req.putheader("Accept", "text/xml")
    req.putheader("User-Agent", "xsc.py")
    req.putheader("Content-length", str(len("n=" + strXMLRequest)))
    req.endheaders()

    # send XML as POST data
    req.send("n=" + strXMLRequest)

    # get HTTP response
    ec, em, h = req.getreply()

    # content-length indicates number of
    # bytes in response XML message
    cl = h.get("content-length", "0")

    # stats us [http-code, http-msg, content-length]
    self.stats = ("[" + str(ec) + " " +
                 str(em) + " " +
                 str(cl) + " bytes]")

    # attempt to read XML response
    nfd = req.getfile()
    try:
      textlines = nfd.read()
      nfd.close()
      # return XML data
      return textlines

    except:
      # return after exception
      nfd.close()
      return ""

# cmd line operation
if  __name__ == "__main__":
  # instantiate server
  xc = xsc()
  xc.server = "localhost:2112"

  # read in the message file
  fd = open(sys.argv[1], "r")
  xmlmsg = fd.read()
  fd.close()

  # make call to server and print
  # stats, and response
  print "XMLSwitch Server: ", xc.server
  response = xc.sendMessage(xmlmsg)
  print xc.stats
  print "Reponse: "
  print response
