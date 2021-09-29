import xml.etree.ElementTree as ET              # python library that parses XML text into tree
                                                # data is a sample XML 
data = '''<stuff>                             
            <users>
                <user x="2">
                    <id>001</id>
                    <name>Chuck</name>
                </user>
                <user x="7">
                    <id>008</id>
                    <name>Brent</name>
                </user>
            </users>
          </stuff>'''

tree = ET.fromstring(data)
lst = tree.findall("users/user")                # find users and append them into list
print("User count:", len(lst))
for item in lst:                                # traverse through list 
    print("Name:", item.find("name").text)
    print("ID:", item.find("id").text)
    print("Attr: ",item.get("x"))
