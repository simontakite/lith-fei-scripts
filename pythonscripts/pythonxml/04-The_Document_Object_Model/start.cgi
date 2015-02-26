#!/usr/local/bin/python
#
# start.cgi - a Python CGI script

import cgi
import os

from ArticleManager import ArticleManager

HEADER = """\
<html>
<body>
<p>
<table cellspacing="0" cellpadding="1">
  <tr><td>
      <h1>XML Articles</h1>
    </td></tr>
  <tr><td>
      <h3><a href="start.cgi?cmd=va">View All</a>&nbsp;|&nbsp;
          <a href="start.cgi?cmd=pa">Post Article</a></h3>
    </td></tr>
</table>
"""

#
# MAIN
#

# content-type header
print "Content-type: text/html"
print
print HEADER

# retrieve query string
query = cgi.FieldStorage()
if query.has_key("cmd"):
  cmd = query["cmd"].value

  # instantiate an ArticleManager
  am = ArticleManager()

  # do something for each command

  # Command: viewAll - list all articles
  if cmd == "va":
    am.viewAll()

  # Command: viewOne - view one article
  if cmd == "v1a":
    aname = query["af"].value
    am.viewOne(aname)

  # Command: postArticle - view the post-article page
  if cmd == "pa":
    am.postArticle()

  # Command: postData - take an actual article post
  if cmd == "pd":
    print "<p>Thank you for your post!</p>"
    am.postArticleData(query)

else:
  # Invalid selection
  print "<p>Your selection was not recognized.</p>

# close the HTML
print "</body></html>"
