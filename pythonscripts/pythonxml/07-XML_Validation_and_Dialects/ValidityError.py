from xml.parsers.xmlproc.xmlapp import ErrorHandler

"""
ValidityErrorHandler -- implement xmlproc's ErrorHandler Interface
"""
class ValidityErrorHandler(ErrorHandler):

  def warning(self, msg):
    print "<p><b><font color=#FF0000>Warning received!:</b></font>"
    print "<br>" + msg + "</p>"
    self.errors = 0

  def error(self, msg):
    print "<p><b><font color=#aa0000>Error received!:</b></font>"
    print "<br>" + msg + "</p>"
    self.errors = 1

  def fatal(self, msg):
    print "<p><b><font color=#aa0000>Fatal Error received!:</b></font>"
    print "<br>" + msg + "</p>"
    self.errors = 1
