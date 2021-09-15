"""
    program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
    The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
    The program creates a Python dictionary that maps the sender's mail address to a count of the number of times 
    they appear in the file. After the dictionary is produced, the program reads through the dictionary using a 
    maximum loop to find the most prolific committer.
"""

def greatestEmailSender(file):                              # receives file to check
    counter = {}                                            # dictionary declaration
    maxVal = 0                                              # auxiliary var to check
    for line in file:                                       # traverse line by line in file
        if line.startswith("From "):                            
            line = line.split()                             # lines that start with 'From' are splited into lists separated by words
            counter[line[1]] = counter.get(line[1],0)+1     # check if dictionary contains second element of line, if not, append it and count it, otherwise increment counter 
    for key, value in counter.items():                      # navigate through dictionary on each key and value
        if value > maxVal:
            maxKey = key
            maxVal = value
    print(maxKey, maxVal)

def main():
    name = input("Enter file:")
    if len(name) < 1:
        name = "mbox-short.txt"
    handle = open(name)
    greatestEmailSender(handle)

if __name__ == "__main__":
    main()