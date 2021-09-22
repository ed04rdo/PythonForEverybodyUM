"""
    Python program that uses urllib to read the HTML from http://py4e-data.dr-chuck.net/known_by_Kararose.html,
    extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to 
    the first name in the list, follow that link and repeat the process n times and report the last name found. 
"""

import urllib.request, urllib.error, urllib.parse        
import ssl                                              
from bs4 import BeautifulSoup                               # python library for pulling data out of HTML and XML files

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False                          
ctx.verify_mode = ssl.CERT_NONE

url = input("ENTER -")
for times in range(7):
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup("a")
    url = tags[17].get("href", None)
    print(url)

    
