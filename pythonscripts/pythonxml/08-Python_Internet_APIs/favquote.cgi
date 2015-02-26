#!/usr/bin/python

import cgi
form = cgi.FieldStorage()
favquote = form["favquote"].value

print "Content-type: text/html"
print ""
print "<html><body>"
print "Your quote is:"
print favquote
print "</body></html>"
