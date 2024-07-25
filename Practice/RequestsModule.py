import requests

# to request a response from the server, there are mainly two methods:
# GET : to request data from the server.
# POST : to submit data to be processed to the server.
# to make HTTP requests in python, we can use several HTTP libraries like:
# httplib, urllib, requests

r = requests.get("https://financialmodelingprep.com/api/v3/quote/AAPL?apikey=a9343db071b7a60643e76aebc0ec6e3a")
print(r.text)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
print(r.json())

# x = requests.get('https://w3schools.com/python/demopage.htm')
# print(x.text)

"""# defining the api-endpoint
API_ENDPOINT = "http://pastebin.com/api/api_post.php"

# your API key here
API_KEY = "ef1aa6ccd2e129aab395f251ea039416"

# your source code here
source_code = ''' 
print("Hello, world!") 
a = 1 
b = 2 
print(a + b) 
'''

# data to be sent to api
data = {'api_dev_key': API_KEY,
        'api_option': 'paste',
        'api_paste_code': source_code,
        'api_paste_format': 'python'}

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT, data=data)

# extracting response text
pastebin_url = r.text
print("The pastebin URL is:%s" % pastebin_url)"""
