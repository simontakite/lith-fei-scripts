#!/usr/local/bin/python
# flat2xml-1.cgi

import cgi
import os
import sys

#
# Start HTTP/HTML Output
#
print "Content-type: text/html"
print
print "<html><body>"

#
# Parse query string for flat file
#
try:
  query = cgi.FieldStorage()
  flatfile = query.getvalue("flatfile", "")[0]
except:
  print "Conversion request not found or incorrectly formatted."
  print "</body></html>"
  sys.exit(0)

#
# Display flat file
#
print "<h1>Flat File</h1>"
print "<p>Flat file received:</p>"
print "<p><pre>" + flatfile + "</pre></p>"
print "</body></html>"
