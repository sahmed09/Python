import os

# This program search for a specific word throughout all files
# In this case we search for "binod"


def is_binod(filename):
    with open(filename, "r") as f:
        fileContent = f.read()

    # Detect all forms of binod
    if "binod" in fileContent.lower():
        return True
    else:
        return False


if __name__ == '__main__':
    # Listing the contents of this folder
    dir_content = os.listdir()

    nBinod = 0
    # For each text file, run isBinod() for them
    for item in dir_content:
        if item.endswith("txt"):
            print(f"Detecting Binod in {item}")
            flag = is_binod(item)
            if flag:
                print(f"Binod found in {item}")
                nBinod += 1
            else:
                print(f"Binod not found in {item}")

    print("\n********* Binod Detector Summary *********")
    print(f"{nBinod} files found with Binod hidden into them.")
