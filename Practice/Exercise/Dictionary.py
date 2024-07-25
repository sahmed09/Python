dictionary = {
    "set": "a set is a well-defined collection of distinct objects",
    "map": "A map is a symbolic depiction emphasizing relationships between elements of some space",
    "tuple": "a tuple is a finite ordered list of elements",
    "list": "a list is created by placing all the items (elements) inside square brackets []",
    "dictionary": "A dictionary is a collection which is unordered, changeable and indexed"
}

inp = input("What you are looking for? ").lower()

if inp in dictionary:
    print(dictionary[inp])
else:
    print("Word not found")

"""try:
    inp = input("What you are looking for? ").lower()

    for keys in dictionary:
        result = keys.find(inp)
        if result != -1:
            print(dictionary[inp])
except:
    print("Not found")"""
