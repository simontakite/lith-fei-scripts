from xml.parsers.xmlproc.xmlapp import DTDConsumer
from xml.parsers.xmlproc.xmlapp import ErrorHandler

"""
BadOrderErrorHandler -- implement xmlproc's ErrorHandler Interface
"""
class BadOrderErrorHandler(ErrorHandler):
  def warning(self, msg):
    print "Warning received!:", msg

  def error(self, msg):
    print "Error received!:", msg

  def fatal(self, msg):
    print "Fatal Error received!:", msg


"""
DTDHandler -- implements xmlproc's DTDConsumer Interface
"""
class DTDHandler(DTDConsumer):
  def __init__(self, parser):
    self.parser = parser

  def dtd_start(self):
    print "Starting DTD..."

  def dtd_end(self):
    print "Finished DTD..."

  def new_general_entity(self, name, val):
    print "General Entity Received: ", name

  def new_external_entity(self, ent_name, pub_id, sys_id, ndata):
    print "External Entity Received: ", ent_name

  def new_element_type(self, elem_name, elem_cont):
    print "New Element Type Declaration: ", elem_name
    print "Content Model: ", elem_cont

  def new_attribute(self, elem, attr, a_type, a_decl, a_def):
    print "New Attribute Declaration: ", attr
