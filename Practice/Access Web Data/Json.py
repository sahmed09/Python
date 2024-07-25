import json
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# JSON in Python
# Python has a built-in package called json, which can be used to work with JSON data.

# Parse JSON - Convert from JSON to Python
# If you have a JSON string, you can parse it by using the json.loads() method.
# The result will be a Python dictionary.
print("JSON to Python:")
x = '{ "name": "John", "age":30, "city":"New York"}'  # some JSON:
y = json.loads(x)  # parse x:
print(y)
print(y["age"])  # the result is a Python dictionary
print(type(y))

# Convert from Python to JSON
# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
print("\nPython to JSON:")
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}  # # a Python object (dict):
y = json.dumps(x)  # convert into JSON:
print(y)  # the result is a JSON string
print(type(y))
print()

# Convert Python objects into JSON strings, and print the values
print(json.dumps({"name": "John", "age": 30}))  # dictionary to json
print(json.dumps(["apple", "bananas"]))  # list to json
print(json.dumps(("apple", "bananas")))  # tuple to json
print(json.dumps("hello"))  # string to json
print(json.dumps(42))  # int to json
print(json.dumps(31.76))  # float to json
print(json.dumps(True))  # True to json
print(json.dumps(False))  # False to json
print(json.dumps(None))  # None to json
print()

# Convert a Python object containing all the legal data types
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x))
print()

# Format the Result
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x, indent=4))  # Use the indent parameter to define the numbers of indents
print()

# can also define the separators, default value is (", ", ": "),
# means using a comma and a space to separate each object,a colon and a space to separate keys from values
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
print(json.dumps(x, indent=4, separators=(". ", " = ")))
print()

# Order the Result
x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
# sort_keys parameter to specify if the result should be sorted or not
print(json.dumps(x, indent=4, sort_keys=True))
print()

# json.load() takes a file object and returns the json object.
f = open("j.json")  # Opening JSON file
data = json.load(f)  # returns JSON object as a dictionary
print(data)
for i in data["cars"]:  # Iterating through the json list
    print(i)
f.close()  # Closing file
