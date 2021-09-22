import re

file = open('mbox-short.txt')
# use regular expression instead of find()
"""
for line in file:
    line = line.rstrip()
    if re.search('From:', line):
        print(line)
"""

# use regular expression instead of startswith()
"""
for line in file:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
"""

"""
    use regular expression to find lines that start with 'X'
    followed by any character zero or more times and the ':'

for line in file:
    line = line.rstrip()
    if re.search('^X.*:', line):
        print(line)
"""
"""
    use regular expression to find lines that start with 'X'
    followed by '-', followed by any character except whitespace
    one or more times and the ':'

for line in file:
    line = line.rstrip()
    if re.search('^X-\S+:', line):
        print(line)
"""
"""
    use regular expression to find digits in a string and return
    them in a list with function findall(), then look for one or 
    more uppercase vowels

x = "My 2 favorite numbers are 4 and 18"
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+',x)
print(y)
"""
"""
    Greedy vs Non greedy example in regular expressions, greedy will
    always return largest possible string. In these case while looking
    for the ':' it returns string until last coincidence.

x = "From: Using the : character : test greedy"
y = re.findall('^F.+:',x) 
print("Greedy return: ")
print(y)
y = re.findall('^F.+?:',x) 
print("Non-Greedy return: ")
print(y)
"""
"""
    Extract string with any non whitespace character one or more times
    followed by '@' and again any non whitespace character one or more
    times.

x = "From eduardo.ra.04@gmail.com Sat Jun 5 09:12:45 2009"
y = re.findall('\S+@\S+',x)
print(y)
"""
"""
    As complement to last expression, parentheses tells where to start 
    and stop string extraction.
    Following expression looks for email addressess on lines that start
    with 'From' but retrieves just the address, excluding 'From'

x = "From eduardo.ra.04@gmail.com Sat Jun 5 09:12:45 2009"
y = re.findall('^From (\S+@\S+)',x)
print(y)
"""
"""
    Three different regular expressions to retrieve just the domain of an 
    email address.

x = "From eduardo.ra.04@gmail.com Sat Jun 5 09:12:45 2009"
y = re.findall('@([\S]+)',x)
print("First method: ",y)
y = re.findall('@([^ ]*)',x)
print("Second method: ",y)
y = re.findall('^From .*@([^ ]*)',x)
print("Third method: ",y)
"""
"""
    In case we´re searching for a '(', '^', '$', '+', '*', etc. the \helps
    taking the character literally

x = "We just received $10.00 for cookies."
y = re.findall('\$[0-9.]+',x)
print(y)
"""
"""
    Exercise for finding spam confidence maximum value in file
"""
file = open("mbox-short.txt")
numlist = []
for line in file:
    line = line.rstrip()
    strVal = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line) # findall() returns an empty list when coincidence not found
    if len(strVal) != 1: continue                               # for omitting empty lists in rest of cycle   
    numlist.append(float(strVal[0]))
print("Maximum confidence value: ", max(numlist))

