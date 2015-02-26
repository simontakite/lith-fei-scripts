#!/usr/local/bin/python
# xlst.cgi

import cgi
import os
import sys

from xml.xslt.Processor import Processor

# parse query string & instantiate xlst proc
query = cgi.FieldStorage()

xsltproc = Processor()

print "Content-type: text/html\r\n"

mode = query.getvalue("mode", "")
if not mode:
  print "<html><body>"
  print "<p>No mode given</p>"
  print "</html></body>"
  sys.exit()

if mode[0] == "show":
  # run XML through simple stylesheet
  xsltproc.appendStylesheetUri("story.xsl")
  html = xsltproc.runUri("story.xml")
  print html

if mode[0] == "change":
  # change XML source file, rerun stylesheet and show
  newXML  = '<?xml version="1.0"?>\n'
  newXML += "\t<story>\n\t<title>"
  newXML += query.getvalue("title")[0] + "</title>\n"
  newXML += "\t<body>\n"
  newXML += query.getvalue("body")[0] + "\n\t</body>\n</story>\n"
  fd = open("story.xml", "w")
  fd.write(newXML)
  fd.close()
  
  # run updated XML through simple stylehseet
  xsltproc.appendStylesheetUri("story.xsl")
  html = xsltproc.runUri("story.xml")
  print html

if mode[0] == "edit":
  # run XML through form-based stylesheet
  xsltproc.appendStylesheetUri("edstory.xsl")
  html = xsltproc.runUri("story.xml")
  print html

    


