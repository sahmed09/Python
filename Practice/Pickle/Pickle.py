import pickle

# Python pickle module is used for serializing and de-serializing a Python object structure.
# Any object in Python can be pickled so that it can be saved on disk.
# What pickle does is that it “serializes” the object first before writing it to file.
# Pickling is a way to convert a python object (list, dict, etc.) into a character stream.
# this character stream contains all the information necessary to reconstruct the object in another python script.
# It is advisable not to unpickle data received from an untrusted source as they may pose security threat.
# the pickle module has no way of knowing or raise alarm while pickling malicious data.

"""Python3 program to illustrate store efficiently using pickle module.  
Module translates an in-memory Python object into a serialized byte stream—a string of  
bytes that can be written to any file-like object"""


def store_data():
    # initializing data to be stored in db
    omkar = {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}
    jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}

    # database
    db = {}
    db['omkar'] = omkar
    db['jagdish'] = jagdish

    # Its important to use binary mode
    dbfile = open('examplePickle', 'ab')

    # source, destination
    pickle.dump(db, dbfile)
    dbfile.close()


def load_data():
    # for reading also binary mode is important
    dbfile = open('examplePickle', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys, '=>', db[keys])
    dbfile.close()


if __name__ == '__main__':
    store_data()
    load_data()


print("\nPickling without a file:")
# initializing data to be stored in db
omkar = {'key': 'Omkar', 'name': 'Omkar Pathak', 'age': 21, 'pay': 40000}
jagdish = {'key': 'Jagdish', 'name': 'Jagdish Pathak', 'age': 50, 'pay': 50000}

# database
db = {}
db['omkar'] = omkar
db['jagdish'] = jagdish
# print(db)

# For storing
b = pickle.dumps(db)  # type(b) gives <class 'bytes'>
# print(type(b))

# For loading
my_entry = pickle.loads(b)
for keys in my_entry:
    print(keys, '=>', my_entry[keys])
# print(my_entry)


#  Pickle a simple list:
print("\nPickle and Unpickle a simple list:")
mylist = ['a', 'b', 'c', 'd']
with open('datafile.txt', 'wb') as fh:
    pickle.dump(mylist, fh)

# Unpickle a simple list:
pickle_off = open("datafile.txt", "rb")
emp = pickle.load(pickle_off)
print(emp)
pickle_off.close()


# Pickle a simple dictionary:
print("\nPickle and Unpickle a simple dictionary:")
EmpID = {1: "Zack", 2: "53050", 3: "IT", 4: "38", 5: "Flipkart"}
pickling_on = open("EmpID.pickle", "wb")
pickle.dump(EmpID, pickling_on)
pickling_on.close()

# Unpickle a dictionary:
pickle_off = open("EmpID.pickle", 'rb')
EmpID = pickle.load(pickle_off)
print(EmpID)
pickle_off.close()

""" Exceptions: Pickle.PicklingError, Pickle.UnpicklingError, EOFError"""
