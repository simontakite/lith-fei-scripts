"""
HTTPServer.py - an simple implementation
of the BaseHTTPServer module
"""

from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler
import string

"""
class myRequestHandler - Handles any and all request
    coming in, regardless of path, file, or request
    method (GET/POST)
"""
class myRequestHandler(BaseHTTPRequestHandler):
  """
  do_GET will be called if the browser does a GET
  request.
  """
  def do_GET(self):
    # give them back a 200 OK every time.
    self.printCustomHTTPResponse(200)

    # start HTML output
    self.wfile.write("<html><body>")
    self.wfile.write("<p>Hello, I am a web server, sort of.</p>")
    self.wfile.write("<p>GET string: " + self.path + "</p>")

    # show browser headers
    self.printBrowserHeaders()

    # finish off HTML
    self.wfile.write("</html></body>")

  """
  do_POST is called if the browser is POSTing data
  from a form
  """
  def do_POST(self):
    # send back a 200 OK
    self.printCustomHTTPResponse(200)

    # start HTML and show browser headers again
    self.wfile.write("<html><body>")
    self.printBrowserHeaders()
    self.wfile.write("<b>Post Data:</b><br>")

    # track down length of the post, so that you
    # can read in the correct number of bytes.  The
    # length of the post is in the browser header
    # named 'content-length'.
    if self.headers.dict.has_key("content-length"):
       # convert content-length from string to int
       content_length = string.atoi(self.headers.dict["content-length"])

       # read in the correct number of bytes from the client
       # connection and send it back to the browser
       raw_post_data = self.rfile.read(content_length)
       print("[Post Data:]", raw_post_data)
       self.wfile.write(raw_post_data)

    # finish off HTML
    self.wfile.write("</html></body>")

  """
  printBrowserHeaders - this method prints the HTTP
      headers sent by the client
  """
  def printBrowserHeaders(self):
    # iterate through header dictionary and
    # display the name and value of each pair.
    self.wfile.write("<p>Headers: <br>")
    header_keys = self.headers.dict.keys()
    for key in header_keys:
      self.wfile.write("<b>" + key + "</b>: ")
      self.wfile.write(self.headers.dict[key] + "<br>")

  """
  printCustomHTTPResponse - this method takes a response
      code and sends the code and custom headers
      back to the browser
  """
  def printCustomHTTPResponse(self, respcode):
    # send back appropriate HTTP code
    self.send_response(respcode)

    # tell them we're sending HTML
    self.send_header("Content-type", "text/html")

    # describe the server software in use!
    self.send_header("Server", "myRequestHandler :-)")

    # close off headers
    self.end_headers()


# start the server on port 2112, requires browser URLs
# to be addressed as http://servername:2112/pathtofile
myServer = HTTPServer(('', 2112), myRequestHandler)

# loop to handle 5 requests
for lp in range(5):
  myServer.handle_request()
