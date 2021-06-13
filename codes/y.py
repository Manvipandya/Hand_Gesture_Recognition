# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 17:27:28 2021

@author: Admin
"""

# Import Module
import os
import cv2
from decimal import Decimal
from PIL import Image
# Folder Path
path = "E:/BE_PROJECT/Cropped_Labelled_Images"
  
# Change the directory
os.chdir(path)
  
from os import listdir
from os.path import isfile, join
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
xyz = []
for i in onlyfiles:
    xyz.append(i[0])  
#print(xyz)

j = 0
y = []
y.append(j)
for w in range(len(xyz)-1) :
    if xyz[w] != xyz[w+1]:
        j+=1
    y.append(j)

print(y)  
print(len(y))  
    

