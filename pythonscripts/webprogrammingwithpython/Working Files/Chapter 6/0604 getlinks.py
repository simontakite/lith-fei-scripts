import urllib, htmllib, formatter

#website = urllib.urlopen("http://www.profmcmillan.com")
website = urllib.urlopen("http://www.uninett.no")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
for link in ptext.anchorlist:
   print(link)
