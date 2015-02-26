"""
CustomerProfile.py
"""
import dbi
import odbc
import StringIO

from xml.dom                 import implementation
from xml.dom.ext             import PrettyPrint
from xml.dom.ext.reader.Sax2 import FromXml

#
# define some global members for the class
CONNECTION_STRING = "Profiles/webuser/w3bus3r"
FIRSTNAME         = 0
LASTNAME          = 1
ADDRESS1          = 2
ADDRESS2          = 3
CITY              = 4
STATE             = 5
ZIP               = 6
CUSTOMER_ID       = 7

class CustomerProfile:
  """
  CustomerProfile - manages the storage and retrieval
  of XML customer profiles from a relational database.
  """
  def getProfileAsDom(self, strId):
    """
    This method calls getProfile with the
    dom option set on, which causes getProfile
    to return its created DOM object, and not
    an XML string
    """
    return self.getProfile(strId, 1)

  def getProfile(self, strId, dom=0):
    """
    getProfile - returns an XML profile chunk
    based on the supplied id.  Returns null if
    not found.
    """
    if not strId:
      return None

    # generate connection
    conn = odbc.odbc(CONNECTION_STRING)
    cmd = conn.cursor()
    cmd.execute("select * from customer where " +
                "customerId = '" + strId + "'")
    conn.close()

    # get data record
    prof_fields = cmd.fetchone()
    if prof_fields is None:
      return None

    # generate XML from fields
    # generate CustomerProfile doctype
    doctype = implementation.createDocumentType(
      "CustomerProfile", "", "CustomerProfile.dtd")

    # generate new document with doctype
    newdoc = implementation.createDocument(
      "", "CustomerProfile", doctype)
    rootelem = newdoc.documentElement

    # create root element id attribute
    rootelem.setAttribute("id", prof_fields[CUSTOMER_ID])

    # create dictionary with field values
    fields = ["firstname", prof_fields[FIRSTNAME],
              "lastname",  prof_fields[LASTNAME],
              "address1",  prof_fields[ADDRESS1],
              "address2",  prof_fields[ADDRESS2],
              "city",      prof_fields[CITY],
              "state",     prof_fields[STATE],
              "zip",       prof_fields[ZIP],
              ]
    # loop through dictionary adding elements and element text
    for pos in range(0, len(fields), 2):
      # create the element
      thisElement = newdoc.createElement(fields[pos])

      # check for empty values and convert to soft nulls
      if fields[pos + 1] is None:
        fields[pos + 1] = ""
      # append field value to element as child text node
      thisElement.appendChild(newdoc.createTextNode(fields[pos+1]))
      rootelem.appendChild(thisElement)

    # return DOM or String based on how we were called...
    if dom:
      return newdoc.documentElement
    else:
      # return string
      strXML = StringIO.StringIO()
      PrettyPrint(newdoc.documentElement, strXML)
      return strXML.getvalue()

  def insertProfile(self, strXML):
    """
    insertProfile takes an XML chunk as a string,
    parses down its fields, and inserts it into the
    profile database.  Raises an exception if XML is
    not well-formed, or customer Id is missing, or if
    SQL execution fails.  Returns 1 on success, 0 on failure.
    """
    if not strXML:
      raise Exception("XML String not provided.")

    # Beign parsing XML
    try:
      doc = FromXml(strXML)
    except:
      print "Error parsing document."
      return 0

    # Normalize whitespace and retrieve root element
    doc.normalize()
    elem = doc.documentElement

    # Extract values from XML packet
    customerId = elem.getAttributeNS(None, 'id')
    firstname = self.extractNodeValue(elem, "firstname")
    lastname  = self.extractNodeValue(elem, "lastname")
    address1  = self.extractNodeValue(elem, "address1")
    address2  = self.extractNodeValue(elem, "address2")
    city      = self.extractNodeValue(elem, "city")
    state     = self.extractNodeValue(elem, "state")
    zip       = self.extractNodeValue(elem, "zip")

    # prepare SQL statement
    strSQL = ("insert into Customer values ("
              "'" + firstname  + "', "
              "'" + lastname   + "', "
              "'" + address1   + "', "
              "'" + address2   + "', "
              "'" + city       + "', "
              "'" + state      + "', "
              "'" + zip        + "', "
              "'" + customerId + "')")

    # generate connection
    conn = odbc.odbc(CONNECTION_STRING)
    cmd = conn.cursor()

    # execute SQL statement
    if (not cmd.execute(strSQL)):
      raise Exception("SQL Exec failed.")

    conn.close()
    return 1

  def extractNodeValue(self, elem, elemName):
      """
      Internal method to parse UNIQUE elements for text value or
      substitute empty strings.
      """
      e = elem.getElementsByTagName(elemName)[0].firstChild
      if e is None:
        return ""
      else:
          return e.nodeValue

  def updateProfile(self, strXML):
    """
    This convenience function accepts a new customer
    profile XML packet.  It extracts the customer ID
    and then calls deleteProfile and insertProfile using
    the new XML.  The return value for the insert is propagated
    back to the caller, unless the delte fails, in which case
    it is propagated back and insert is never called.
    """
    # parse document for customer Id
    try:
      doc = FromXml(strXML)
      customerId = doc.documentElement.getAttributeNS('','id')
    except:
      print "Error parsing document."
      return 0

    # attemp delte and insert based on customerId
    if self.deleteProfile(customerId):
      return self.insertProfile(strXML)
    else:
      return 1

  def deleteProfile(self, strId):
    """
    deleteProfile accepts a customer profile ID
    and deletes the corresponding record in the database.
    Returns 1 on success, 0 on failure.
    """
    if not strId:
      return 0

    # generate database connection
    conn = odbc.odbc(CONNECTION_STRING)
    cmd = conn.cursor()
    ok = cmd.execute("delete from customer where customerId = '"
                     + strId + "'")):
    conn.close()
    return ok and 1 or 0
