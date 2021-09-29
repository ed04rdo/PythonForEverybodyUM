"""
    Python program that prompts for a URL, reads the JSON data from that URL using 
    urllib and then parses and extracts the comment counts from the JSON data, compute 
    the sum of the numbers in the file.
"""
import urllib.request, urllib.parse, urllib.error                      # libraries for requesting, parsing and handling url errors
import json                                                            # library for serialization and deserialization of json objects
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input("Address: ")                                           # address 
print("Retrieving",address)
uh = urllib.request.urlopen(address)                                   # urlopen() returns file requested 
data = uh.read().decode()                                              # reading file and decoding it from UTF8 to unicode string

try:
    js = json.loads(data)                                              # loads() deserializes JSON format
except:
    js = None

print(type(js["comments"]))
sum = 0
for dict in js["comments"]:                                            # from dictionary js extract list of dictionaries to traverse it 
    sum += dict["count"]

print(sum)

