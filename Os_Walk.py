import os

for folderName, subfolders, filenames in os.walk("C:\\Users\\edixish\\Documents\\Automation\\Romania Rules"):
    print(folderName)
    # # print(type(subfolders)) # LIST
    for Sub_inside in subfolders:
        print(Sub_inside)
    for file in filenames:
        print(file)

