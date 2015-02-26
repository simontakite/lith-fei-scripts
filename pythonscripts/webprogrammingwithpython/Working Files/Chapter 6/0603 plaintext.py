import htmllib, urllib, formatter, sys

website = urllib.urlopen("http://www.ntnu.no")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.DumbWriter(sys.stdout))
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
ptext.close()
