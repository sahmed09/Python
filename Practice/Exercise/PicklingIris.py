import requests
import pickle

"""
download the file from the link and save in text file. Then make a list of lists and then pickle it.
Finally read the pickled file.
"""

data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
# print(data)

l1 = data.split("\n")  # converting to a list by spliting \n
# print(l1)

l2 = [item.split(",") for item in l1 if len(item) != 0]
print(l2)

with open("iris.pkl", "wb") as f:
    pickle.dump(l2, f)

# To read this pickle file:
"""with open("iris.pkl", "rb") as f:
    # print(f)
    print(pickle.load(f))"""
