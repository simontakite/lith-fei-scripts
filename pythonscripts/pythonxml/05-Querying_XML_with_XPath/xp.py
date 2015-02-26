"""
xp.py (requires xml doc on stdin)
"""
import sys

from xml.dom.ext.reader import PyExpat
from xml.xpath          import Evaluate

path0 = "ship/captain"  # all captain elements
path1 = "ship/captain/text()"
path2 = "ship[2]/captain/text()"
path3 = 'ship[class="Intrepid"]'
path4 = 'ship[class="Constitution"]/@name'
path5 = 'ship[@name="USS Enterprise"]'
path6 = "/shiptypes//captain"
path7 = "ship[@name='USS Voyager']/../@name"

reader = PyExpat.Reader()
dom = reader.fromStream(sys.stdin)


captain_elements = Evaluate(path0, dom.documentElement)
for element in captain_elements:
  print "Element: " element


captainnodes = Evaluate(path1, dom.documentElement)
for captainnode in captainnodes:
  print "Starfleet Captain: ", captainnode.nodeValue


capnode = Evaluate(path2, dom.documentElement)
print "Captain of ship[2] is: ", capnode[0].nodeValue


shipnodes = Evaluate(path3, dom.documentElement)
for shipnode in shipnodes:
  shipname = shipnode.getAttribute("name")
  captain = Evaluate("captain/text()", shipnode)
  print "------------ Intrepid Class Ship ------------"
  print "Name: ", shipname
  print "Captain: ", captain[0].nodeValue


ship = Evaluate(path4, dom.documentElement)
print "Name of Constitution Class Ship: ", ship[0].nodeValue


ships = Evaluate(path5, dom.documentElement)
for shipnode in ships:
  registry = Evaluate("registry-code/text()", shipnode)
  captain = Evaluate("captain/text()", shipnode)
  print "Found Enterprise with registry: ", registry[0].nodeValue
  print "Captain: ", captain[0].nodeValue


captains = Evaluate(path6, dom.documentElement)
for captain in captains:
  print "Captain: ", captain.firstChild.nodeValue


org = Evaluate(path7, dom.documentElement)
print "USS Voyager is owned by", org[0].nodeValue
