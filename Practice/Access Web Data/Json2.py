import urllib.request, urllib.parse, urllib.error
import json

data = '''
{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print(info)
print('Name:', info['name'])
print('Email:', info['email']['hide'])
print('Phone:', info['phone']['number'])
print()

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
print('User Counts:', len(info))
for item in info:
    print('Name:', item['name'])
    print('ID:', item['id'])
    print('Attribute:', item['x'])
print()


"""In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/json2.py.
 The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract 
 the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below"""

# Sample data:
address = 'http://py4e-data.dr-chuck.net/comments_42.json'
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None

# print(json.dumps(js, indent=4))
print('No of Comments:', len(js['comments']))
lst = list()
for item in js['comments']:
    lst.append(int(item['count']))
print(lst)
print('Sum:', sum(lst))
print()

# Actual data:
address = ' http://py4e-data.dr-chuck.net/comments_835927.json'
print('Retrieving', address)
uh = urllib.request.urlopen(address)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
try:
    js = json.loads(data)
except:
    js = None

# print(json.dumps(js, indent=4))
print('No of Comments:', len(js['comments']))
lst = list()
for item in js['comments']:
    lst.append(int(item['count']))
print(lst)
print('Sum:', sum(lst))
print()
