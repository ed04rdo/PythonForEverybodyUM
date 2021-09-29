"""
    API that takes a rough approximation of an address, cleans it up and returns
    formal details of the address, like GPS coordinates, etc.
"""

import urllib.request, urllib.parse, urllib.error                          # libraries for requesting, parsing and handling url errors
import json                                                                # library for serialization and deserialization of json objects
import ssl                                                                 

api_key = False                                                            # substitute in case of having an API key

if api_key is False:                                                        
    api_key = 42                                                           # values provided by professor  
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :                                                                     # if using google api anf having API key
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

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

    print("Retrieving",url)
    uh = urllib.request.urlopen(url, context=ctx)                          # urlopen() returns file requested 
    data = uh.read().decode()                                              # reading file and decoding it from UTF8 to unicode string
    print("Retrieved:",len(data),"characters")

    try:
        js = json.loads(data)                                              # loads() deserializes JSON format
    except:
        js = None
    
    if not js or 'status' not in js or js["status"] != 'OK':               # check js status 
        print("==== FAILED TO RETRIEVE ====")
        print(data)
        continue

    print(json.dumps(js, indent=4))                                        # serialize obj to a JSON formatted string

    lat = js["results"][0]["geometry"]["location"]["lat"]                  # navigate through js to extract latitude
    lng = js["results"][0]["geometry"]["location"]["lng"]                  # navigate through js to extract longitude
    print("lat=",lat,",lng=",lng)
    location = js["results"][0]["formatted_address"]                       # navigate through js to extract formatted address
    print(location)


