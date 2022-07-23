from pathlib import Path
import pandas as pd  # pip install pandas

import glob
import os

# os.chdir(r'D:/master thesis/ani files only/RAW Data/ARRAy 043 files_Tested at 77oC_Standard Array')  
# input_dir = list(glob.glob("*.dta"))


# # input_dir = glob.glob("C:/Users/pasiv/Desktop/ARRAy 043 files_Tested at 77oC_Standard Array*.txt")
# print(input_dir)
---------------------------------------------------------------------------------------
# Import Module
import os

# Folder Path
path = "C:/Users/pasiv/Desktop/ARRAy 043 files_Tested at 77oC_Standard Array"

# Change the directory
os.chdir(D:/master thesis/ani files only/RAW Data/ARRAy 043 files_Tested at 77oC_Standard Array)

# Read text File


def read_text_file(file_path):
  with open(file_path, 'r') as f:
    print(f.read())


# iterate through all file
for file in os.listdir():
  # Check whether file is in text format or not
  if file.endswith(".dta"):
    file_path = f"{path}\{file}"

    # call read text file function
    print(read_text_file(file_path))

------------------------------------------------------------------------------
import os
FILENAMES=[]

for root, dirs, files in os.walk(r"D:/master thesis/ani files only/RAW Data/ARRAy 043 files_Tested at 77oC_Standard Array"):
    # print(files)
 
    for filename in files:
         if(filename.endswith(".dta")):
             FILENAME.append(filename)
             print(FILENAME)
print('\n')    
    
for FILENAME in FILENAMES:
    print(FILENAME," contains the following functions:\n")
    f1=open(FILENAME,'r')
    for line in f1:
       if ("Pt") in line:
          print (line)
       else:
          pass
    print('\n')
    f1.close()