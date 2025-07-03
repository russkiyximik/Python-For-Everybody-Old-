import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defauts to certicate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = input("Enter count - ")
position = input("Enter position (1st, 2nd, ..., nth) - ")

for i in range(int(count)):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[int(position) - 1].get('href', None)
    print(url)