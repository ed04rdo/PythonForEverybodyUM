def slicing(s):
    print(s[0:3])   # second number "up to but not including"
    print(s[-1])    # last value   
    print(s[0:500]) # second number is beyond the end of string, stops at the end
    print(s[:4])    # from beginning to 4 
    print(s[4:])    # from 4 to end
    print(s[:])     # all string

def inOperator(s):
    # "in" operator checks if one string is in another string, returns boolean
    containsN = 'n' in s
    containsE = 'e' in s
    containsUpperE = 'E' in s
    print(containsN)
    print(containsE)
    print(containsUpperE)

def stringFunctions(s):
    lowerCase = s.lower()                # functions apply for constants & variables
    upperCase = s.upper()                # toUpperCase
    pos = s.find('ui')                   # returns position of first ocurrence for substring in string, -1 if not found
    rep = s.replace('Eduardo','Gerardo') # replaces ALL ocurrences of first parameter with second parameter
    rmSpace = s.strip()                  # ' hi ', strip() removes whitespaces from left & right, lstrip() left, rstrip() right
    start = s.startswith('E')            # BOOLEAN checks if string starts with substring given
    dir(s)                               # dir() shows the methods of the class, in this case <'str'>


def main():
    s = input("INGRESE UNA CADENA:")
#   slicing(s)
#   inOperator(s)
    stringFunctions(s)

if __name__== "__main__":
    main()