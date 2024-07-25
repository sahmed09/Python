import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

"""In this assignment you will write a Python program that expands on http://www.py4e.com/code3/urllinks.py.
The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor
tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link
 and repeat the process a number of times and report the last name you find."""

# Sample problem:
# Ignore SSL certificate errors:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter URL: ')
url = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
# count = int(input("Enter count: "))
# position = int(input("Enter position: ")) - 1
count = 4
position = 3 - 1

while count >= 0:
    print('Retrieving:', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # for tag in tags:
    #     print(tag.get("href", None))
    url = tags[position].get("href", None)
    count = count - 1
print()


# Actual problem:
# Ignore SSL certificate errors:
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter URL: ')
URL = "http://py4e-data.dr-chuck.net/known_by_Breagh.html"
# count = int(input("Enter Count: "))
# position = int(input("Enter Position: ")) - 1
count = 7
position = 18 - 1  # position starts from 1, index from 0, so -1 to match with position

while count >= 0:
    print("Retrieving: ", URL)
    html = urllib.request.urlopen(URL, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    # for tag in tags:
    #     print(tag.get("href", None))
    URL = tags[position].get('href', None)
    count = count - 1
