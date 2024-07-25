import os


def create_if_not_exist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)


def move(folder_name, files):
    for file in files:
        os.replace(file, f"{folder_name}/{file}")


if __name__ == '__main__':
    
    files = os.listdir()
    files.remove("AutomaticFolderCleaner.py")
    # print(files)

    create_if_not_exist('Images')
    create_if_not_exist('Docs')
    create_if_not_exist('Media')
    create_if_not_exist('Others')

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
    # print(images)

    docExts = [".txt", ".doc", ".docx", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
    # print(docs)

    mediaExts = [".flv", ".mp3", ".mp4"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
    # print(medias)

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in imgExts) and (ext not in docExts) and (os.path.isfile(file)):
            others.append(file)
    # print(others)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)
