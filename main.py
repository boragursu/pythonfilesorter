import os
import re
import shutil
import json

with open("path.txt") as file: #Remember to update path from path.txt!!!
    FOLDER_PATH = file.read()
    filenamelist = os.listdir(FOLDER_PATH)


subjectinput=str(input("Please write the name of the class: "))
patterninput=str(input("Please write file name pattern: "))
if subjectinput!="" and patterninput!="":
  with open('subjectFile.json') as subjectFile:
    data=json.load(subjectFile)

  if subjectinput not in data.keys():
    data[subjectinput]=[patterninput]
  else:
    data[subjectinput].append(patterninput)  

  with open('subjectFile.json', 'w') as subjectFile:
    json.dump(data,subjectFile)
  
with open('subjectFile.json') as subjectFile:
  data=json.load(subjectFile)
  for j in data:
    for i in data[j]:
        pattern=i
        for filename in filenamelist:
            x = re.search(pattern, str(filename))
            if x:
                if os.path.exists(FOLDER_PATH+"/"+j) == False:
                  try:
                    os.mkdir(FOLDER_PATH+"/"+j)
                  except OSError:
                    print ("Creation of the directory %s failed" % FOLDER_PATH)
                  else:
                    print ("Successfully created the directory %s " % FOLDER_PATH)
                  shutil.move(FOLDER_PATH+"/"+filename,FOLDER_PATH+"/"+j+"/"+filename)
                else:
                  shutil.move(FOLDER_PATH+"/"+filename,FOLDER_PATH+"/"+j)
                  print("Sucesfully moved to existing subject folder")
            else:
                pass 
