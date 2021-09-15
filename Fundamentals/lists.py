def lists():
    # Lists are MUTABLE, can change content using index operator, strings are NOT MUTABLE
    l1 = [1,2,3,4,5]            # same type
    l2 = ['Orange', 1, 23.4]    # different types
    l3 = [32, 'm', [1,2,3]]     # list into list
    print(len(l1))              # method to retrieve list length
    print(range(4))             # range method retrieves a list of numbers of parameter length
    isThere = 4 in l1           # Boolean that checks if a list contains something
    isNotThere = 10 in l1       # Boolean that checks if a list do not contain something

def slicingLists():
    t = [1,3,5,'wer',78,'awer',987.35, '234']
    print(t[-1])
    print(t[3:7])
    print(t[:])

def stringMethods():
    text = 'String containing many words separated with spaces'
    m = list() 
    s = list()                  # create a new empty list
    s.append('book')            # add item to the end of the list
    s.append(True)
    for x in range(200):
        m.append(x)
    m.sort()                    # order items in list
    maxim = max(m) 
    minim = min(m)
    avg = sum(m)/len(m)         # compute average with list methods
    print(avg)
    divided = text.split()      # breaks string into list of strings, default... 
                                # ...delimiter is blankspace, any other pass by parameter
    for w in divided:
        print(w)

def printDay(f):                 # print days of received mails based on file content
    for found in f:
        if not found.startswith('From ') : continue # if condition body is no longer than 1 line, it can be written in the same line
        day = found.split()
        print(day[2])

def printAddresses(f):
    for found in f:
        if not found.startswith('From ') : continue
        address = found.split()
        divAddress = address[1].split('@')
        print('Address name:', divAddress[0])
        print('address domain:', divAddress[1])

def fileContentInList():        # sort file content in list without repeated words
    fh = open('romeo.txt','r')
    lst = list()
    for line in fh:
        lineList = line.split()
        for word in lineList:
            if not lst.__contains__(word) : lst.append(word)
            else : continue
    lst.sort()
    print(lst)

def main():
    stringMethods()
    file1 = open('mbox-short.txt','r')
    printDay(file1)
    file1.seek(0)
    printAddresses(file1)
    fileContentInList()

if __name__ =='__main__':
    main()