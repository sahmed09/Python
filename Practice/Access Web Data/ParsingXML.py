import xml.etree.ElementTree as et
import ssl
import urllib.request, urllib.parse, urllib.error

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    </phone>
    <email hide="yes" />
</person>'''

tree = et.fromstring(data)
print('Name:', tree.find('name').text)
print('Email:', tree.find('email').get('hide'))
print('Phone:', tree.find('phone').text.strip())
print('Phone type:', tree.find('phone').get('type'))
print()

inp = '''
<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>'''

stuff = et.fromstring(inp)
lst = stuff.findall('users/user')
print(lst)
print('User count:', len(lst))

for item in lst:
    print('Name:', item.find('name').text)
    print('Id:', item.find('id').text)
    print('Attribute:', item.get('x'))
    print()
print()


# Find the geometric location of an address:
# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as et
# import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location(e.g. Dhaka/Bangladesh etc.): ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    if api_key is not False:
        parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    # print(data.decode())
    tree = et.fromstring(data)

    results = tree.findall('result')
    lat = results[0].find('geometry').find('location').find('lat').text
    lng = results[0].find('geometry').find('location').find('lng').text
    location = results[0].find('formatted_address').text

    print('lat', lat, 'lng', lng)
    print(location)
print()


"""In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py.
 The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract 
 the comment counts from the XML data, compute the sum of the numbers in the file."""

# import xml.etree.ElementTree as et
# import ssl
# import urllib.request, urllib.parse, urllib.error

# Sample data:
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "http://py4e-data.dr-chuck.net/comments_42.xml"
params = list()
data = urllib.request.urlopen(address, context=ctx).read()
print('Retrieved', len(data), 'characters')
tree = et.fromstring(data)
# print(data.decode())

results = tree.findall('comments/comment')
print(len(results))
for result in results:
    # print(result.find('count').text)
    params.append(int(result.find('count').text))
print('Sum:', sum(params))
print()


# Actual data:
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = "http://py4e-data.dr-chuck.net/comments_835926.xml"
params = list()
data = urllib.request.urlopen(address, context=ctx).read()
print('Retrieved', len(data), 'characters')
tree = et.fromstring(data)
# print(data.decode())

results = tree.findall('comments/comment')
print(len(results))
for result in results:
    # print(result.find('count').text)
    params.append(int(result.find('count').text))
print('Sum:', sum(params))
