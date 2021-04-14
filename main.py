import os
import re
import shutil

with open("path.txt") as file: #Remember to update path from path.txt!!!
    FOLDER_PATH = file.read()
    filenamelist = os.listdir(FOLDER_PATH)

subjects=["mat","cin","eng","kim","ink","tur","fiz"] #Add subject names here

for pattern in subjects:
    
  for filename in filenamelist:
      x = re.search(pattern, str(filename))
      if x:
          if not os.path.exists(f'{FOLDER_PATH}/{pattern}'):
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
