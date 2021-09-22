import re

def sum(file):
    s = 0
    for line in file:
        numsOnLine = re.findall('[0-9]+',line)
        if len(numsOnLine) == 0: continue
        """
            map applies given function to given iterable on each of its elements
            in this case helps casting string to int, but it returns a map object
            that needs to be casted to list so it can be iterated in next line. 
        """
        numsOnLine = list(map(int,numsOnLine))  
        for n in numsOnLine:
            s = s + n
    return s

def main():
    name = input("Type the name of the file: ")
    file = open(name)
    print(sum(file))

if __name__ == "__main__":
    main()