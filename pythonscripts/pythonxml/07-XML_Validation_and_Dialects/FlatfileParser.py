#
# FlatfileParser.py
#
from xml.dom     import implementation

class FlatfileParser:
  def parseFile(self, fileAsString):

    # Create DocType Declaration
    doctype = implementation.createDocumentType('BillSummary', '',
                                                'BillSummary.dtd')

    # Create empty DOM Document and get root element
    doc = implementation.createDocument('', 'BillSummary', doctype)
    elemDoc = doc.documentElement

    # boolean text parsing switch to help
    # navigate flat file
    bInElement = 0

    # Read in each line of flat file for processing
    for line in fileAsString.splitlines():
      # Test to see if we're in a section or not
      if bInElement:
        # Check to see if we're leaving a section
        if ':' in line:
          # Append section element, reset section switch
          elemDoc.appendChild(elemCurrent)
          bInElement = 0
        else:
          # Parse a section line on ':'
          k,v = line.split(':')

          # Create element name and child text from key/value pair
          elem = doc.createElement(k.strip())
          elem.appendChild(doc.createTextNode(v.strip()))

          # append element to current section element
          elemCurrent.appendChild(elem)

      # Create a new element based on what section of
      # the flat file we are in...
      section = line.strip()
      if section == "Section: Customer":
        elemCustomer = doc.createElement("Customer")
        bInElement = 1

        # Set current working element for the Customer section
        elemCurrent = elemCustomer

      if section == "Section: Bill Highlights":
        elemBillHighlights = doc.createElement("BillHighlights")
        bInElement = 1

        # Set current working element for the BillHighlights section
        elemCurrent = elemBillHighlights

      if section == "Section: Item":
        elemItem = doc.createElement("Item")
        bInElement = 1

        # Set current working element for the Item section
        elemCurrent = elemItem

    return (doc)        
