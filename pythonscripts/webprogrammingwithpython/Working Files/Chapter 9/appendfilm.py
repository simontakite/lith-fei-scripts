from xml.dom.minidom import Document
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import string, sys


"""
doc = Document()
films = doc.createElement("films")
doc.appendChild(films)
afilm = doc.createElement("film")
films.appendChild(afilm)
title = doc.createElement("title")
afilm.appendChild(title)
text = doc.createTextNode("Annie Hall")
title.appendChild(text)
director = doc.createElement("director")
afilm.appendChild(director)
text = doc.createTextNode("Woody Allen")
director.appendChild(text)
year = doc.createElement("year")
afilm.appendChild(year)
text = doc.createTextNode("1977")
year.appendChild(text)
filename = "films.xml"
f = open(filename, "w")
f.write(doc.toprettyxml(indent="   "))
f.close()
"""

doc = Document()
#doc.setContentHandler(handler)
#doc.parse(open('films.xml'))
films = doc.getElementsByTagName("films")
afilm = doc.createElement("film")
films.appendChild(afilm)
title = doc.createElement("title")
afilm.appendChild(title)
text = doc.createTextNode("Annie Hall")
title.appendChild(text)
director = doc.createElement("director")
afilm.appendChild(director)
text = doc.createTextNode("Woody Allen")
director.appendChild(text)
year = doc.createElement("year")
afilm.appendChild(year)
text = doc.createTextNode("1977")
year.appendChild(text)
filename = "films.xml"
f.write(doc.toprettyxml(indent="   "))
f.close()
