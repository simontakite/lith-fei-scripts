"""
 runxs.py
"""
import XMLSwitchHandler
import BaseHTTPServer

# start up
print "XMLSwitch starting..."
XMLSwitchServer = BaseHTTPServer.HTTPServer(
    ('', 2112), XMLSwitchHandler.XMLSwitchHandler)

# run server
print "Running..."
for x in range(10):
  XMLSwitchServer.handle_request()
