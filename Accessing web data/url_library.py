import urllib.request, urllib.parse, urllib.error

# Count words from an online file
file = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")
count = {}
for line in file:
    words = line.decode().split()
    for word in words:
        count[word] = count.get(word,0)+1
print(count)