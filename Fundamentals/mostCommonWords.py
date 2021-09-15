def wordCounter(file):
    counter = {}                                                        # declare dictionary 
    for line in file:                                                   # traverse file line by line
        line = line.split()                                             # clean from whitespaces and line jumps
        for word in line:                                              
            counter[word] = counter.get(word,0)+1                       # add words to dictionary and count repeated
    return counter

def mostCommonWords(dict):
    """
        list comprehension changing position between key and value and 
        append them on a list, then sort the list in reverse order and
        assign the result to tmp
    """
    tmp = sorted([(v, k) for k, v in dict.items()], reverse = True) 
    for val, key in tmp[:10]:                                           # traverse first 10 values of list of tuples 
        print(key+":", val)

def main():
    file = open('Quit India.txt', encoding = 'cp850')                   # encoding is for an error on a character unabled to read 
    count = wordCounter(file)
    mostCommonWords(count)

if __name__ == "__main__":
    main()