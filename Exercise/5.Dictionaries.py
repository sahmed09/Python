"""A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with
curly brackets, and they have keys and values. No duplicate members."""

dic = {}
print(type(dic))

dic = dict()
print(type(dic))

my_dict = {"Car1": "Audi", "Car2": "BMW", "Car3": "Mercidies Benz"}
print(type(my_dict))
print(my_dict)

# Access the item values based on keys
print(my_dict['Car1'])

# We can even loop through the dictionaries keys
for x in my_dict:
    print(x)

# We can even loop through the dictionaries values
for x in my_dict.values():
    print(x)

# We can also check both keys and values
for x in my_dict.items():
    print(x)

# Adding items in Dictionaries
my_dict['car4'] = 'Audi 2.0'
print(my_dict)

# Update value
my_dict['Car1'] = 'MAruti'
print(my_dict)

"""Nested Dictionary"""
car1_model = {'Mercedes': 1960}
car2_model = {'Audi': 1970}
car3_model = {'Ambassador': 1980}

car_type = {'car1': car1_model, 'car2': car2_model, 'car3': car3_model}
print(car_type)

# Accessing the items in the dictionary
print(car_type['car1'])
print(car_type['car1']['Mercedes'])
