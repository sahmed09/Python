# Python does not have built-in support for Arrays, but Python Lists can be used instead
cars = ["Ford", "Volvo", "BMW"]
print(cars)

# Access the Elements of an Array
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)

cars[0] = "Toyota"  # Modify the value of the first array item
print(cars)

# The Length of an Array
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

# Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)

# Adding Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")  # append() method to add an element to an array
print(cars)

# Removing Array Elements
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)  # pop() method to remove an element from the array
print(cars)

cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")  # remove() method to remove an element from the array
print(cars)
