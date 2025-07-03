import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}
for line in fhand:
    print(line.decode().strip())
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

for k, v in sorted(counts.items()):
    print(k, v)
# How to sort uppercase and lowercase alphabetically together?