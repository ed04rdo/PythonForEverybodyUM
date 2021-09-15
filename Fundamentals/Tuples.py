# items() method in dictionary returnslist of tuples
# sorted() sorts by key    
"""
    tuple comparison:

        >>> (0, 1, 2) < (5, 1, 2)                   # left to right Most Significant Value check 
        True
        >>> (0, 1, 20000) < (0, 3, 4)               # if first is the same, checks with next       
        True
        >>> ('Jones', 'Sally') > ('Adams', 'Sam')
        True
"""

def sortByKey(dict):
    for key, val in sorted(dict.items()):
        print(key, val)

def sortByVal(dict):
    tmp = []
    for key, val in dict.items():
        tmp.append((val,key))
    print(sorted(tmp))

def main():
    (x, y) = (4, 'Fred')
    (a, b) = (99, 98) 
    d = {'a':10, 'f':1, 'e':22, 'b':3, 'd':7, 'c':4}
    sortByKey(d)
    sortByVal(d)

if __name__ == "__main__":
    main()

