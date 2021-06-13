# -*- coding: utf-8 -*-
"""
Created on Tue May 11 14:00:26 2021

@author: Admin
"""



# Import Module
import os
import cv2
import PIL
import glob
from decimal import Decimal
from PIL import Image
# Folder Path
#path = "E:/BE_PROJECT/Final ISL/1"
  
# Change the directory
#os.chdir(path)
  
# Read text File

directory = "G:/Final ISL"  

def read_text_file(file_path,i,name1):
    with open(file_path, 'r') as f:
        Fil = os.path.splitext(file)
        name = directory + '/' + name1 + '/'
        name = name + Fil[0] + '.jpg'
        name1 = name1  + str(i) + '.jpg'
        if name != name1:
            os.rename(name,name1)
        #print('name = ' + name)
        print(name1)
        
  
  
# iterate through all file

for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        i=1
        path = os.path.join(root, subdirectory)
        os.chdir(path)
        for file in os.listdir():
            file_path = f"{path}\{file}"
            name1 = path[13:]
            read_text_file(file_path,i,name1)
            i+=1