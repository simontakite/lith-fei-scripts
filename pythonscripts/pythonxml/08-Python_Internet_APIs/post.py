"""
post.py
"""
from httplib import HTTP
from urllib  import quote

# establish POST data
myquote = 'This is my quote: "I think therefore I am."'

# be sure not to quote the key= sequence...
postdata = "favquote=" + quote(myquote)

print "Will POST ", len(postdata), "bytes:"
print postdata

# begin HTTP request
req = HTTP("127.0.0.1")  # change to your IP or localhost
req.putrequest("POST", "/c8/favquote.cgi")
req.putheader("Accept", "text/html")
req.putheader("User-Agent", "MyPythonScript")

# Set Content-length to length of postdata
req.putheader("Content-Length", str(len(postdata)))
req.endheaders()

# send post data after ending headers,
# CGI script will receive it on STDIN
req.send(postdata)

ec, em, h = req.getreply()
print "HTTP RESPONSE: ", ec, em

# get file-like object from HTTP response
# and print received HTML to screen
fd = req.getfile()
textlines = fd.read()
fd.close()
print "\nReceived following HTML:\n"
print textlines
