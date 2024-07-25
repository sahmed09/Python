import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# sample data for testing:
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
lis = []
# Retrieve all of the anchor tags
tags = soup('tr')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    number = tag.contents[1]
    # print('Contents:', number)
    number = re.findall('[0-9]+', str(number))
    # print(number)
    lis.extend(number)
    # print('Attrs:', tag.attrs)
print(lis)
total = 0
for item in lis:
    if len(item) != 0:
        total = total + int(item)
print(total)
print()


# Actual data for testing:
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_835924.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
lis = []
# Retrieve all of the anchor tags
tags = soup('tr')
for tag in tags:
    # Look at the parts of a tag
    # print('TAG:', tag)
    # print('URL:', tag.get('href', None))
    number = tag.contents[1]
    # print('Contents:', number)
    number = re.findall('[0-9]+', str(number))
    # print(number)
    lis.extend(number)
    # print('Attrs:', tag.attrs)
print(lis)
total = 0
for item in lis:
    if len(item) != 0:
        total = total + int(item)
print(total)
print()
