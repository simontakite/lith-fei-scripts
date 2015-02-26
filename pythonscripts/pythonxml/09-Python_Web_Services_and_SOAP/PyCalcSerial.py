"""
Python MSSOAP Serializer Example
"""
# import support for COM
import win32com.client

# SOAP Action URI
BaseSoapActionUri = "http://tempuri.org/action/Calc."

# Namespace
WrapperElementNamespace = "http://tempuri.org/message/"

# Service End Point
EndPointUrl = \
  "http://centauri/MSSoapSamples/Calc/Service/SrSz/AspVbs/Calc.asp"

# Calculate(operation, value1, value2)
#   Takes an operator (as a word like "Add") along
#   with two values and returns the result
def Calculate(Op, Val1, Val2):
  # Instantiate HttpConnector
  connector = win32com.client.Dispatch("MSSOAP.HttpConnector")

  # Set properties (will fail if makepy.py wasn't run
  #                 on SOAP type library)
  connector.SetProperty("EndPointURL", EndPointUrl)
  connector.SetProperty("SoapAction", BaseSoapActionUri + Op)

  # Start SOAP message
  connector.BeginMessage()

  # Create a serialization object
  serializer = win32com.client.Dispatch("MSSOAP.SoapSerializer")

  # Attach it to the connector created earlier
  serializer.Init(connector.InputStream)

  # Create SOAP Envelope
  serializer.startEnvelope()
  serializer.startBody()
  serializer.startElement(Op, WrapperElementNamespace, '', "m")
  serializer.startElement("A")
  serializer.writeString(Val1)
  serializer.endElement()
  serializer.startElement("B")
  serializer.writeString(Val2)
  serializer.endElement()
  serializer.endElement()
  serializer.endBody()
  serializer.endEnvelope()

  # Finsih SOAP message
  connector.EndMessage()

  # Create SOAP reader object
  reader = win32com.client.Dispatch("MSSOAP.SoapReader")
  reader.Load(connector.OutputStream)

  # check for errors
  if reader.Fault:
    print "Error: ", reader.faultstring.Text

  # Return calculation value
  return reader.RPCResult.Text

# Main line-- do some calculations
print "Using Service End Point:", EndPointUrl
print "Calculate 3 * 4: \t",
print Calculate("Multiply", 3, 4)

print "Calculate 4 - 3: \t",
print Calculate("Subtract", 4, 3)

print "Calculate 345 + 1004: \t",
print Calculate("Add", 345, 1004)

print "Calculate 115 / 5: \t",
print Calculate("Divide", 115, 5)
