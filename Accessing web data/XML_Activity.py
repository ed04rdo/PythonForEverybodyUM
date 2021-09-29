"""
    Python program that prompts for a URL, reads the XML data from that URL using urllib
    and then parse and extract the comment counts from the XML data, compute the sum of 
    the numbers in the file. 
    TESTED WITH 
        http://py4e-data.dr-chuck.net/comments_42.xml 
        http://py4e-data.dr-chuck.net/comments_1347872.xml
"""
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("ENTER ADDRESS:")
xml = urllib.request.urlopen(url,context=ctx).read()
tree = ET.fromstring(xml)
lst = tree.findall(".//count")                  # find users and append them into list using XPath syntax for XML
count = 0
for item in lst:                                # traverse through list 
    count = count + int(item.text)
print(count)