import os


def soldier(path, file, format):
    """path - folder location in which we want to change the file names or prettify
        file - file location where all the file names are saved which we don't want to change
        format - specify format in which we want to operate"""

    os.chdir(path)  # getting directory path
    i = 1
    files = os.listdir(path)  # files will become list

    # getting the file names in a list format which i don't want to change
    with open(file) as f:
        filelist = f.read().split("\n")

    # searches for file names in ext.txt file which i don't want change
    for file in files:
        if file not in filelist:
            os.rename(file, file.capitalize())

        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i += 1


soldier(r"E:\PycharmProjects\Practice\Exercise\Test", r"E:\PycharmProjects\Practice\Exercise\ext.txt", ".png")

