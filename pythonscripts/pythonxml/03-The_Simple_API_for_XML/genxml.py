"""
genxml.py

Descends PyXML tree, indexing source files and creating
XML tags for use in navigating the source.
"""

import os
import sys

from xml.sax.saxutils import escape


def quoteattr(data):
  # Based on quoteattr() from xml.sax.saxutils from Python 2.2.
  '''Escape and quote an attribute value.

  Escape &, <, and > in a string of data, then quote it for use as
  an attribute value.  The " character will be escaped as well, if
  necessary.
  '''
  data = escape(data)
  if '"' in data:
    if "'" in data:
      data = '"%s"' % data.replace('"', "&quot;")
    else:
      data = "'%s'" % data
  else:
    data = '"%s"' % data
  return data


def process(filename, fp):
  print "* Processing:", filename

  # parse the file
  pyFile = open(filename)
  fp.write("<file name=\"" + filename + "\">\n")
  inClass = 0
  line = pyFile.readline()
  while line:
    line = line.strip()
    if line.startswith("class") and line[-1] == ":":
      if inClass:
        fp.write(" </class>\n")
      inClass = 1
      fp.write(" <class name='" + line[:-1]  + "'>\n")

    elif line.startswith("def") and line[-1] == ":" and inClass:
      fp.write("  <method name=" + quoteattr(line[:-1]) + "/>\n")

    line = pyFile.readline()

  pyFile.close()
  if inClass:
    fp.write(" </class>\n")
    inClass = 0

  fp.write("</file>\n")

def finder(fp, dirname, names):
  """Add files in the directory dirname to a list."""
  for name in names:
    if name.endswith(".py"):
      path = os.path.join(dirname, name)
      if os.path.isfile(path):
        process(path, fp)

def main():
  print "[genxml.py started]"

  xmlFd = open("pyxml.xml", "w")
  xmlFd.write("<?xml version=\"1.0\"?>\n")
  xmlFd.write("<pyxml>\n")

  os.path.walk(sys.argv[1], finder, xmlFd)

  xmlFd.write("</pyxml>")
  xmlFd.close()

  print "[genxml.py finished]"

if __name__ == "__main__":
  main()
