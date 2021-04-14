import os
import re

with open("path.txt") as file:
    FOLDER_PATH = file.read()

    filenamelist = os.listdir(FOLDER_PATH)
for filename in filenamelist:
    x = re.search(r"apple", str(filename))
    if x:
        print(filename)
    else:
        pass
