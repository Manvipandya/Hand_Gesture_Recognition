# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 18:36:14 2021

@author: Admin
"""


# Import Module
import os
import cv2
from decimal import Decimal
from PIL import Image
# Folder Path
#path = "E:/BE_PROJECT/Final ISL/1"
  
# Change the directory
#os.chdir(path)
  
# Read text File

directory = "E:/BE_PROJECT/Final ISL/"  

def read_text_file(file_path,i,name1):
    with open(file_path, 'r') as f:
        Fil = os.path.splitext(file)[0]
        name = Fil + '.JPG'
        img = cv2.imread(name)
        name1 = name1 + '_' + str(i) + '.jpg'
        cv2.imwrite("E:/BE_PROJECT/abc/" + name1 , img)
        print(name1)
        
  
  
# iterate through all file

for root, subdirectories, files in os.walk(directory):
    for subdirectory in subdirectories:
        i=1
        path = os.path.join(root, subdirectory)
        os.chdir(path)
        for file in os.listdir():
            file_path = f"{path}\{file}"
            name1 = path[24:]
            read_text_file(file_path,i,name1)
            i+=1
            if i>50 :
                break