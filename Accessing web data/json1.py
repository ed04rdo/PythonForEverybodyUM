import json                                     # python library for handling json objects 

# JSON example text
data = '''
    [
        {   "name" : "Chuck",
            "id" : "001",
            "phone" : {
                "type" : "intl",
                "number" : "+1 734 303 4456"
            },
            "email" : {
                "hide" : "yes"
            }
        },
        {
            "name" : "Claire",
            "id" : "002",
            "phone" : {
                "type" : "intl",
                "number" : "+1 457 303 4525"
            },
            "email" : {
                "hide" : "no"
            }
        }
    ]
        '''
info = json.loads(data)                         # loads() returns a python dictionary

for user in info:
    print("Name:", user["name"])
    print("ID:", user["id"])
    print("Hide:",user["email"]["hide"])