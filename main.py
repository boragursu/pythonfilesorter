import os
import re
import shutil
with open("path.txt") as file: #Remember to update path from path.txt!!!
    FOLDER_PATH = file.read()
    filenamelist = os.listdir(FOLDER_PATH)

subjects={} 
subjectinput=str(input("Please write the name of the class: "))
patterninput=str(input("Please write file name pattern: "))
if subjectinput not in subjects.keys():
  subjects[subjectinput]=[patterninput]
else:
  subjects[subjectinput].append(patterninput)

for j in subjects:
   for i in subjects[j]:
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
