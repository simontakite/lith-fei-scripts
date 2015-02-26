# ArticleManager.py
import os
from urllib  import quote
from article import Article
from storage import Storage

class ArticleManager:
  """Manages articles for the web page.

  Responsible for creating, loading, saving, and displaying
  articles."""

  def viewAll(self):
    """Displays all XML files in the current working directory."""
    print "<p>View All<br><br>"

    # grab list of files in current directory
    fl = os.listdir(".")
    for xmlFile in fl:
      # weed out XML files
      tname, ext = os.path.splitext(xmlFile)
      if ext == ".xml":
        # create HTML link surrounding article name
        print '<br><a href="start.cgi?cmd=v1a&af=%s">%s</a><br>' \
              % (quote(xmlFile), tname)

  def viewOne(self, articleFile):
    """Takes an article file name as a parameter and
    creates and displays an article object for it.
    """
    # create storage and article objects
    store = Storage()
    art = store.load(articleFile)

    # Write the HTML to browser (standard output)
    print "<p>Title: " + art.title + "<br>"
    print "Author: " + art.author + "<br>"
    print "Date: " + art.time + "<br>"
    print "<table width=500><tr><td>" + art.contents
    print "</td></tr></table></p>"

  def postArticle(self):
    """Displays the article posting form."""
    print POSTING_FORM

  def postArticleData(self, form):
    """Accepts actual posted form data, creates and
    stores an article object."""
    # populate an article with information from the form
    art = Article()
    art.title       = form["title"].value
    art.author      = form["author"].value
    art.contributor = form["contrib"].value
    art.contents    = form["contents"].value

    # store the article
    store = Storage()
    store.save(art)

POSTING_FORM = '''\
<form method="POST" action="start.cgi?cmd=pd">
<p>
Title:      <br><input type="text" length="40" name="title"><br>
Contributor:<br><input type="text" length="40" name="contrib"><br>
Author:     <br><input type="text" length="40" name="author"><br>
Contents:   <br><textarea rows="15" cols="80" name="contents"></textarea><br>
<input type="submit">
</form>
'''
