"""
 sp.py - a series of web pages and forms that send messages
  to the XML Switch for data access.
"""
import os
import cgi

from xsc                     import xsc
from XMLMessage              import XMLMessage
from xml.dom.ext.reader.Sax2 import FromXml

def doLogin(id):
  """
   doLogin(id) - this method grabs a user's profile
   and displays it as XML on the browser, and also
   provides a form that allows the user to edit their
   own data.
  """

  # Bring up XML Switch client
  xs = xsc()
  xs.server = "centauri:2112"

  # prepare an XML message for the server
  xmlmsg = XMLMessage()

  # format a getProfile message
  xmlmsg.setXMLMessage("""
       <message>
         <header><rpc/></header>
         <body>
           <object class="CustomerProfile"
             method="getProfile">
             <param>""" + id + """</param>
           </object>
         </body>
       </message>
                       """)

  # Display how CGI is contacting XML switch
  print "<p>Message to be sent on your behalf:<br><xmp>"
  print xmlmsg.getXMLMessage()
  print "</xmp></p>"

  # make the call to the XML Switch
  xmlresp = xs.sendMessage(xmlmsg.getXMLMessage())

  # display response
  print "<P>Response received on your behalf:<br><xmp>"
  print xmlresp
  print "</xmp></p>"

  # setup profile XML Message and retrieve response DOM
  xmlmsg.setXMLMessage(xmlresp)
  msgdom = xmlmsg.getXMLMessageDom()

  # Create a form to edit this new profile data
  print "<h1>Edit your profile</h1>"
  print "<form action='sp.py' method='GET'>"
  print "<table width=450 border=1>"

  # parse result
  try:
    CustProfElement = msgdom.getElementsByTagName("CustomerProfile")[0]
    CustProfElement.normalize()

    # pick out ID number
    id = CustProfElement.getAttributeNS(None, "id")
    print "<tr>"
    print " <td colspan=2><b>Greetings " + id + "</b></td>"
    print "</tr>"

    # iterate through children, creating pre-populated
    # form as we go...
    nodes = CustProfElement.childNodes
    for node in nodes:
      if node.nodeType == node.ELEMENT_NODE:
        print "<tr><td>"
        print "<b>" + node.nodeName + "</b>"
        print "</td><td>"
        for ec in node.childNodes:
          print "<input type=text size=20 name='" + node.nodeName  + "' "
          print " value='" + ec.nodeValue + "'>"

        print "</td></tr>"
  except:
     print "<tr><td>Exception</td><td>Encountered</td></tr>"

  # finish up the form
  print "<tr><td colspan=2>"
  print "<input type=submit value='update profile'>"
  print "<input type=hidden name='id' value='" + id + "'>"
  print "<input type=hidden name='mode' value='updateProf'>"
  print "</td></tr>"
  print "</table>"
  print "</form>"


def doUpdateProfile():
  """
   doUpdateProfile() - this method is called to update a profile
   using the updateProfile XML message.
  """
  print "<p>Update message on your behalf:<br><xmp>"

  xmlmsg =  "<message><header><rpc/></header>\n"
  xmlmsg += "<body><object class='CustomerProfile' method='updateProfile'>\n"
  xmlmsg += "<param><CustomerProfile id="
  xmlmsg += "'" + id[0] + "'>\n"
  xmlmsg += "<firstname>" + qs.get("firstname","")[0].strip() + "</firstname>\n"
  xmlmsg += "<lastname>"  + qs.get("lastname","")[0].strip()  + "</lastname>\n"
  xmlmsg += "<address1>"  + qs.get("address1","")[0].strip()  + "</address1>\n"
  xmlmsg += "<address2>"  + qs.get("address2","")[0].strip()  + "</address2>\n"
  xmlmsg += "<city>"      + qs.get("city","")[0].strip()      + "</city>\n"
  xmlmsg += "<state>"     + qs.get("state","")[0].strip()     + "</state>\n"
  xmlmsg += "<zip>"       + qs.get("zip","")[0].strip()       + "</zip>\n"
  xmlmsg += "</CustomerProfile></param></object></body></message>"
  print xmlmsg
  print "</xmp></p>"

  print "Update in progress..."

  xs = xsc()
  xs.server = "centauri:2112"
  resp = xs.sendMessage(xmlmsg)
  print "<P>Response received:<br><xmp>"
  print resp
  print "</xmp></p>"

  print "<h1>Log Back In?</h1>"
  print "<form name=login action='/cgi-bin/sp.py' method='GET'>"
  print "Use Current Customer ID:<br>"
  print "<input type='text' size='15' name='id'"
  print " value='" + id[0] + "'>&nbsp;"
  print "<input type=submit value=' login '>"
  print "<input type='hidden' name='mode' value='login'>"
  print "</form>"

def doGetOffers():
  print "<p>Retrieving all offers...</p>"
  xs = xsc()
  xs.server = "centauri:2112"

  xmlmsg =  str("""<message>
                     <header><rpc/></header>
                       <body>
                         <object class="XMLOffer"
                          method="getAllOffers">
                         </object>
                       </body>
                     </message>""")
  resp = xs.sendMessage(xmlmsg)

  print "<p>Fromatting response from server..."
  print "<h1>Offers!</h1>"

  offdom = FromXml(resp)
  offers = offdom.getElementsByTagName("offer")

  for offer in offers:
    offer.normalize()
    for node in offer.childNodes:
      if (node.nodeType == node.ELEMENT_NODE):
        if (node.nodeName == "heading"):
          print "<h3>" + node.firstChild.nodeValue + "</h3>"
        if (node.nodeName == "description"):
          print "<p>" + node.firstChild.nodeValue + "</p>"

# ''''''''''''''''''''''''''''''''''''''''''''
# MAIN
#
qs   = cgi.parse_qs(os.environ["QUERY_STRING"])
mode = qs.get("mode", "")
id   = qs.get("id", "")

print "Content-type: text/html"
print ""
print "<html>"
print """<HEAD><TITLE>SuperUltraMegaCorp Shopping Portal (intro.html)
          </TITLE></HEAD><BODY>"""
print """<P align="center"><h1>SuperUltraMegaCorp Shopping Portal</h1></P>"""
print """<p><h3>click <a href='/intro.html'>here</a> to login</h3>"""
print """   <h3>click <a href='/cgi-bin/sp.py?mode=getOffers'>here</a>
                to review offers
            </h3></p>"""

if mode[0] == "updateProf":
  doUpdateProfile()

if mode[0] == "login":
  doLogin(id[0])

if mode[0] == "getOffers":
  doGetOffers()

print "</body></html>"
