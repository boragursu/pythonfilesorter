import os
import re
import shutil

pattern = "cin"
with open("path.txt") as file:
    FOLDER_PATH = file.read()

    filenamelist = os.listdir(FOLDER_PATH)
for filename in filenamelist:
    x = re.search(pattern, str(filename))
    if x:
        if os.path.exists(FOLDER_PATH+"/"+pattern) == False:
          try:
            os.mkdir(FOLDER_PATH+"/"+pattern)
          except OSError:
            print ("Creation of the directory %s failed" % FOLDER_PATH)
          else:
            print ("Successfully created the directory %s " % FOLDER_PATH)
          shutil.move(FOLDER_PATH+"/"+filename,FOLDER_PATH+"/"+pattern+"/"+filename)
        else:
          shutil.move(FOLDER_PATH+"/"+filename,FOLDER_PATH+"/"+pattern)
          print("Sucesfully moved to existing subject folder")
    else:
        pass
