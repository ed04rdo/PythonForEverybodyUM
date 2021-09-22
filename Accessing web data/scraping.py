# parsing web pages
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup                           # python library for pulling data out of HTML and XML files


# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("Enter: ")
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')               # retrieves a soup object with information of the page cleaned or parsed

tags = soup('a')                                        # retrieves all the anchor tags
for tag in tags:                                        # iterates over the anchor tags found
    print(tag.get("href", None))                        # print href values 