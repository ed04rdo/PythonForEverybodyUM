def findLineBeginning(f):
    #fString = file1.read()            # interprets file object as string (uncomment if used)
    count = 0
    # for loop interprets a file as a sequence of lines  
    for line in f:                     # finds & prints lines that start with desired substring
        if line.startswith('From'):
            print(line.strip())
            count = count+1

def fileToUpper():
    fname = input("Enter file name: ")
    f = open(fname, 'r')
    for line in f:
        print(line.rstrip().upper())
    f.close()

def findSubstring(f):
    for line in f:                 # finds & prints lines that contain substring
        if not line.__contains__("@uct.ac.za"):
            continue
        print(line.strip())

def excludeSubstring(f):
    for line in f:                 # finds & prints lines that do not start with substring
        if not line.startswith('From'):
            print(line.strip())
            count = count+1

def avg(f):
    count = 0
    avg = 0
    for line in f:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        pos = line.find("0.")
        avg = avg + float(line[pos:])
        count = count+1
    avg = avg/count
    print("Average spam confidence:", avg)

def main():
    """
        After the first call, the input is exhausted. In order to execute 
        more functions with the same file it´s needed to seek back to the 
        beginning before another call
    """
    file1 = open('mbox-short.txt','r') # opens it as file object, requires file and mode r-> read w-> write r+-> read&write a -> append
    print("Learning file handling\n")
    avg(file1)
    print("\n")
    file1.seek(0)
    findLineBeginning(file1)


if __name__ == '__main__':
    main()