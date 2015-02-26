#!/usr/local/bin/python
# flat2xml-2.cgi

import cgi
import os
import sys

from FlatfileParser      import FlatfileParser
from xml.dom.ext         import PrettyPrint
from xml.parsers.xmlproc import xmlval
from ValidityError       import ValidityErrorHandler

# customer failure message
def failure(msg):
  print "<h1>Failure</h1>"
  print "<p><b>Post received, Failure called:"
  print msg + "</b></p>"

# customer success message
def success(msg):
  print "<p><b>XML Document Received, is valid, and "
  print "has been written to disk. "
  print "Message: " + msg + "</b></p>"

#
# Start HTTP/HTML Output
#
print "Content-type: text/html"
print
print "<html>"
print "<body>"

#
# Parse query string for flat file
#
try:
  query = cgi.FieldStorage()
  flatfile = query.getvalue("flatfile", "")
except:
  failure("Conversion request not found or incorrectly formatted.")
  print "</body></html>"
  sys.exit(0)

# instatiate flat file parser & display file
ffp = FlatfileParser()
print "<h1>Flat File</h1>"
print "<p>Flat file received:</p> "
print "<p><pre>" + flatfile + "</pre></p>"

#
# Convert flatfile to XML
#
print "<h1>Conversion</h1>"
BillSummaryDOM = ffp.parseFile(flatfile)
CustomerIdElement = BillSummaryDOM.getElementsByTagName("customer-id")
if CustomerIdElement:
  # go after the Customer Id
  CustomerId = CustomerIdElement[0].firstChild.data
  print "<p>Converted to XML...</p>"
else:
  # No id found, boot document now
  failure("Unable to detect customer-id in DOM instance.")
  print "</body></html" 
  sys.exit(0)  

#
# Validate the dom
#
print "<h1>Validation</h1>"
try:
  # Write document to disk based on Customer Id
  fd = open(CustomerId + ".xml", 'w')
  PrettyPrint(BillSummaryDOM, fd)
  fd.close()
except:
  # Problem writing document?
  failure("<p>Unable to write XML document to disk.</p>")
  print "</body></html>"
  sys.exit(1)

# instantiate parser
xv = xmlval.XMLValidator()

# instantiate the error handler
veh = ValidityErrorHandler(xv.app.locator)

# set up parser, call parse method
xv.set_error_handler(veh)
xv.parse_resource(CustomerId + ".xml")

# Display XML Document
print "<h1>XML Document</h1><pre><xmp>"
PrettyPrint(BillSummaryDOM)
print "</xmp></pre>"

#
# confirm response to user
#
if hasattr(veh, "errors") and veh.errors:
  failure("Validation Error(s).")
else:
  success("Success.")

# Finish Up
print "</body></html>"
