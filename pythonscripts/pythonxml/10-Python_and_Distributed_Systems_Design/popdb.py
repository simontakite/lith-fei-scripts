"""
popdb.py - populate the Profiles/Customer DB with ODBC calls
"""
import dbi, odbc
conn = odbc.odbc("Profiles/webuser/w3bus3r")
cmd = conn.cursor()

# loop to get input values.
while 1:
  firstname = raw_input("firstname:")
  lastname  = raw_input("lastname:")
  address1  = raw_input("address1:")
  address2  = raw_input("address2:")
  city      = raw_input("city:")
  state     = raw_input("state, 2 letter max:")
  zip       = raw_input("zip, 10 digit max:")
  customerId = raw_input("Customer ID, 40 character max length:")

  # execute SQL statement
  cmd.execute("insert into Customer values('"
              + firstname  + "', '"
              + lastname   + "', '"
              + address1   + "', '"
              + address2   + "', '"
              + city       + "', '"
              + state      + "', '"
              + zip        + "', '"
              + customerId + "')")

  finished = raw_input("another? [y/n]:")
  if (finished == "n"):
    break
