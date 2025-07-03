import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

url = input("Enter URL - ")
rawcontent = urllib.request.urlopen(url, context=ctx).read()
content = json.loads(rawcontent) # We can write content instead of content.decode() because the content is bytes BUT in UTF-8

for i in range(len(content['comments'])):
    print(content['comments'][i]['count'])

print(sum( [int(content['comments'][i]['count']) for i in range(len(content['comments']))]))
