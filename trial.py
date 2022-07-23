import matplotlib.pyplot as plt 
import numpy as np 
import math 
import pandas as pd 
from pathlib import Path
import pandas as pd  #
from sklearn import preprocessing
import glob
import os

directory = 'D:/master thesis/ani files only/RAW Data/ARRAy 043 files_Tested at 77oC_Standard Array'

os.chdir(r'D:/master thesis/ani files only/RAW Data/ARRAy 043 files_Tested at 77oC_Standard Array') 
# input_dir = [] 
input_dir = glob.glob("*.dta")
# print(input_dir)
# print(len(input_dir))


find = "#"
EOL = "EOC"
date = "DATE"
Date = []
Pt=[]
T = [] 
Vf = [] 
Vm = []
Ach = []

Time = []
Freq = []
Zreal = []
Zimag = []
Zmod = []
Zphz = []

# OCV TABLE
for filename in input_dir:
    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        flag = 0
        date_flag = 0
        # print(f)
        for num, line in enumerate(f,1):
            if date_flag != 1:
                if date in line:

                    array = line.split("\t")
                #    Date.append(array[2])
                    dates= array[2]
                    date_flag = 1  
            if flag != 1:
                if  find in line:
                    num = num + 1
                    for num1, table in enumerate(f,num):
                        if EOL in table:
                            flag = 1
                            break
                        else:
                            value = table.split("\t")
                            Pt.append(float(value[1]))
                            T.append(float(value[2]))
                            Vf.append(float(value[3]))
                            Vm.append(float(value[4]))
                            Ach.append(float(value[5]))
                            Date.append(dates)   
            #  print(Vf)
# fig = plt.figure(figsize=(8, 6))
# plt.scatter(T,Vf,marker="o")
# plt.title("Nyquist plot",fontsize=25) 
# plt.xlabel('T')
# plt.ylabel('Vf') 
# plt.show()

            else:                         
            #Z curve impedance data------------------------------------------------------------------------------          
                if  find in line:
                    num = num + 1
                    
                    for num1, table in enumerate(f,num):
                        value = table.split("\t")      #Since data is seperated by tab spaces, using split to organize it into columns.
                        Time.append(float(value[2]))
                        Freq.append(float(value[3]))
                        Zreal.append(float(value[4]))
                        Zimag.append(float(value[5]))
                        Zmod.append(float(value[7]))
                        Zphz.append(float(value[8]))
                        # Date.append()
                        # print(Freq)
print(len(Date))
# print(len(Vf))
# # Zmoda= np.array(Zmod).reshape(-1,1)
# # Timea = np.array(Time).reshape(-1,1)
# scaler = preprocessing.MinMaxScaler()
# normalizedZmod=scaler.fit_transform(Zmoda)
# normalizedtime=scaler.fit_transform(Timea)
fig = plt.figure(figsize=(8, 6))
plt.scatter(Date,Vf,marker="o")
plt.title("Data for OCV curve table in all ANI array files from 2019/09/04 to 2021/06/10",fontsize=25) 
plt.xlabel('Date of measurement')
plt.ylabel('Voltage Vf') 
plt.show()
    
    
    
    
for i in range(length):
    #  # print(i)
    # print(Freq[i])
    # print(Date[i])
    a= Zmod[i]
    b= Freq[i]
    c= Date[i]
    
    #plotting graphs for data   
    
              

    # Zreala= np.array(Zreal[i])
    # Freqa = np.array(Freq[i])
    # Zimaga = np.array(Zimag[i])
    # print(Freqa)
     # plt.plot(Vf[i])   
 