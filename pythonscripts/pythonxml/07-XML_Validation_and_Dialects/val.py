""" xml validation """
import sys
from xml.parsers.xmlproc import xmlval
from xpHandlers import BadOrderErrorHandler, DTDHandler

xv = xmlval.XMLValidator()
dt = DTDHandler(xv.parser)
bh = BadOrderErrorHandler(xv.app.locator)

xv.set_error_handler(bh)
xv.set_dtd_listener(dt)
xv.parse_resource(sys.argv[1])
