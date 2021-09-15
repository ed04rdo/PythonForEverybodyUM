def dictionaries():
    car = dict()                                # declaration 
    car["wheels"] = 4                           # initialization
    car["doors"] = 4
    car["fuel"] = False
    car["maxSpeed"] = 220

    car2 = {"wheels"   : 4,                     # declaration & initialization 
            "doors"    : 2,
            "fuel"     : True,
            "maxSpeed" : 180}
    
    return car,car2

def namesHistogram(f):                          # count name coincidences in file 
    names = {}                                  # declare dictionary
    for name in f:                              # read line
        name = name.strip()                     # clean line of whitespaces & line breaks
        names[name] = names.get(name,0)+1       # get method looks in dictionary for given key, if not in dictionary returns second parameter
    return names

def main():
    file1 = open("names.txt","r")
    n = namesHistogram(file1)
    print("THERE ARE",len(n),"DIFFERENT NAMES")
    for key in n:                               # for loop iterates over the keys of a dictionary
        print(key+":", n[key])
    """
        for key, val in n.items():              # python can iterate over multiple variables
            print(key, val)
    """
    d1,d2 = dictionaries()
    print(d1)
    print(d2)

if __name__=="__main__":
    main()