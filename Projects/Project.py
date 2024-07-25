import re

print("Press 1 for Read the file")
print("Press 2 for Write the file")
print("Press 3 for Search the file")
print("Press 4 for Update the file")
print("Press 5 for Delete the file")
print("Press 0 to exit")
a = int(input("Select your choice what you want to do: "))

if a == 1:
    f = open("project.txt", "r")
    content = f.read()
    f.close()
    print(content)

elif a == 2:
    f = open("project.txt", "a")
    w = input("What you enter in the file? ")
    f.write("\n" + w)
    f.close()
    f = open("project.txt", "r")
    content = f.read()
    f.close()
    print(content)

elif a == 3:
    w = input("What you are searching for? ")
    with open("project.txt", 'r') as file:
        filedata = file.read()
    if re.search(w, filedata):
        print(w, "presents in file")
    else:
        print(w, "doesn't present in file")

elif a == 4:
    w = input("Word you are looking for? ")
    s = input("Word you want to replace to? ")

    with open('project.txt', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(w, s)

    # Write the file out again
    with open("project.txt", "w") as file:
        file.write(filedata)

    with open("project.txt", "r") as file:
        print(file.read())
        file.close()

elif a == 5:
    lis = []
    with open('project.txt', 'r') as file:
        filedata = file.read()
        lis.append(filedata)

else:
    print("Not a valid choice")
