"""
    Program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
    messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a 
    second time using a colon.
    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008 
    Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""

def hourCounter(file):                                          # hour counter, receives file
    hours = {}                                                  # dictionary declaration
    for line in file:                                           # traverse file by line 
        if line.startswith("From "):                            # select desired lines
            line = line.split()                                 # separate by word into list
            hours[line[5][:2]] = hours.get(line[5][:2],0)+1     # check in dictionary first two chars of fifth element in line list
    return hours                                

def printSortedHours(dict):                                     # receive dictionary 
    for key, val in sorted(dict.items()):                       # sort it by key and print it
        print(key, val)

def main():
    name = input("Enter file:")                                 # enter file name by keyboard
    if len(name) < 1:                                               
        name = "mbox-short.txt"
    file = open(name)                                           # open file
    hours = hourCounter(file)
    printSortedHours(hours)

if __name__ == "__main__":
    main()