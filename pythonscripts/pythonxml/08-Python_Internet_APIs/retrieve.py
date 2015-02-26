"""
retrieve.py example
"""
from urllib import urlretrieve

def callback(blocknum, blocksize, totalsize):
  print "Downloaded " + str((blocknum * blocksize)),
  print " of " + totalsize

urlretrieve("http://www.example.com/pyxml.xml", "px.xml", callback)
print "Download Complete"
