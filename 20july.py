import matplotlib.pyplot as plt 
import numpy as np 
import math 
import pandas as pd 
from pathlib import Path
import pandas as pd  # pip install pandas

import glob
import os

directory = 'D:/master thesis/ani files only/RAW Data/ARRAy 043 files_Tested at 77oC_Standard Array'

os.chdir(r'D:/master thesis/ani files only/RAW Data/ARRAy 043 files_Tested at 77oC_Standard Array') 
# input_dir = [] 
input_dir = glob.glob("*.dta")
# print(input_dir)
# print(len(input_dir))
#check

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
                    Date.append(array[2])
                    date_flag = 1  
            if flag != 1:
                if  find in line:
                    num = num + 1
                    t_Pt = []
                    t_T = []
                    t_Vf = []
                    t_Vm = []
                    t_Ach = []
                    for num1, table in enumerate(f,num):
                        if EOL in table:
                            flag = 1
                            break
                        else:
                            value = table.split("\t")
                            t_Pt.append(float(value[1]))
                            t_T.append(float(value[2]))
                            t_Vf.append(float(value[3]))
                            t_Vm.append(float(value[4]))
                            t_Ach.append(float(value[5]))
                            
                    Pt.append(t_Pt)
                    T.append(t_T)
                    Vf.append(t_Vf)
                    Vm.append(t_Vm)
                    Ach.append(t_Ach)   
            else:                          
                #Z curve impedance data------------------------------------------------------------------------------          
                if  find in line:
                    num = num + 1
                    t_Time = []
                    t_Freq = []
                    t_Zreal = []
                    t_Zimag = []
                    t_Zmod = []
                    t_Zphz = []
                    for num1, table in enumerate(f,num):
                        value = table.split("\t")      #Since data is seperated by tab spaces, using split to organize it into columns.
                        t_Time.append(float(value[2]))
                        Freq.append(float(value[3]))
                        t_Zreal.append(float(value[4]))
                        t_Zimag.append(float(value[5]))
                        t_Zmod.append(float(value[7]))
                        t_Zphz.append(float(value[8]))
            
                    Time.append(t_Time)
                    Freq.append(t_Freq)
                    Zreal.append(t_Zreal)
                    Zimag.append(t_Zimag)
                    Zmod.append(t_Zmod)
                    Zphz.append(t_Zphz)
                    # print(Freq)
length = len(Freq)
for i in range(length):
     # print(i)
        # print(Freq[i])
        
    print(len(Zreal))
    print(len(Zimag))
    fig = plt.figure(figsize=(8, 6))
  
  
    plt.plot(Zreal[i],Zimag[i],marker="o")
    plt.title("Nyquist plot",fontsize=25) 
    plt.xlabel('Real values of impedance')
    plt.ylabel('Imaginary values of impedance') 
    plt.show()          
    
    # Zreala= np.array(Zreal[i])
    # Freqa = np.array(Freq[i])
    # Zimaga = np.array(Zimag[i])
    # print(Freqa)
     # plt.plot(Vf[i])   
 


      


        
            
        








# Pt=[]
# T = [] 
# Vf = [] 
# Vm = []
# Ach = []
# Time = []
# Freq = []
# Zreal = []
# Zimag = []
# Zmod = []
# Zphz = []



    
# for i in lines: 
    
    
#     Pt.append(i.split(',')[0])
#     T.append(i.split(','))
#     # Vf.append(i.rstrip().split()) 
#     # Vm.append(i.rstrip().split()) 
#     # Ach.append(i.rstrip().split   ()) 
#     # print()
#     # break
# print(Pt)  
  
# Tarr= np.array(T) #time array consists of the time values in the OCV curve.
# Vfarr= np.array(Vf) #Vf array consists of the voltage values in the OCV curve. 
# Vmarr= np.array(Vm)
# Acharr= np.array(Ach)
# time_array = Tarr.astype(np.float) 
# Vf_array = Vfarr.astype(np.float) 
# print("The time array is:- \n ",(time_array))
# print("The Vf array is:- \n ",(Vf_array)) 
# x= time_array
# y= Vf_array 
# fig = plt.figure(figsize=(8, 6))
# plt.plot(x,y,marker="o")
# plt.title("OCV curve",fontsize=25) 
# plt.xlabel('Time (sec)')
# plt.ylabel('Vf(V vs ref)') 
# plt.show()