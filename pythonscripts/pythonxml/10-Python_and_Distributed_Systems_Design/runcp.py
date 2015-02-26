"""Script to retrieve a CustomerProfile both as XML text and a DOM."""

from CustomerProfile import CustomerProfile
from xml.dom.ext import PrettyPrint

cp = CustomerProfile()

print "String of XML:"
print cp.getProfile("234-E838839")

print "Or retrieve a DOM:"
dom = cp.getProfileAsDom("234-E838839")
PrettyPrint(dom)
