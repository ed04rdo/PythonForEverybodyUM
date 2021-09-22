"""
    Scraping Numbers from HTML using BeautifulSoup. The program uses urllib to read the HTML 
    from the data file in http://py4e-data.dr-chuck.net/comments_1347870.html, and parse the 
    data, extracting numbers and compute the sum of the numbers in the file.
"""
import urllib.request, urllib.parse, urllib.error
import ssl
from bs4 import BeautifulSoup                           # python library for pulling data out of HTML and XML files

# ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input("ENTER: ")
sum, count = 0, 0
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html,'html.parser')

tags = soup("span")
for tag in tags:                                        # iterates over the span tags found
    sum += int(tag.text)                                # cast string text to int and sum it
    count += 1 
print("COUNT",count)
print("SUM", sum)