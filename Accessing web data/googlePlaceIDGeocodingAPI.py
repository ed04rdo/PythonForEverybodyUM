"""
    Calling a JSON API
    Python program that prompts for a location, contacts a web service and retrieves JSON for the web service and parses
    that data, and retrieves the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies 
    a place as within Google Maps.
"""

import urllib.request, urllib.parse, urllib.error                          # libraries for requesting, parsing and handling url errors
import json                                                                # library for serialization and deserialization of json objects
import ssl

api_key = False

if api_key == False:    
    api_key = 42                                                           # values provided by professor  
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'      # if using google api anf having API key

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:                                                                # infinite loop
    address = input("Address: ")                                           # address for consulting on API
    if len(address) < 1: break                                             # pressing enter breaks cycle

    parms = {}                                                             # dictionary
    parms["address"] = address                                             # add address
    if api_key is not False: parms["key"] = api_key                        # add API key
    url = serviceurl + urllib.parse.urlencode(parms)                       # creating valid url format, urlencode() receives dictionary, parses it and returns url format string

    print("Retrieving:",url)
    uh = urllib.request.urlopen(url, context=ctx)                          # urlopen() returns file requested 
    data = uh.read().decode()                                              # reading file and decoding it from UTF8 to unicode string

    try:
        js = json.loads(data)                                              # loads() deserializes JSON format
    except:
        js = None
    
    if not js or 'status' not in js or js["status"] != 'OK':               # check js status 
        print("==== FAILED TO RETRIEVE ====")
        print(data)
        continue

    placeID = js["results"][0]["place_id"]
    print(address,"ID is:",placeID)