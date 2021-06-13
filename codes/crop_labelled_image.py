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
path = "E:\BE_PROJECT\YOLO_LABELIMG"
  
# Change the directory
os.chdir(path)
  
# Read text File
  
  
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        Fil = os.path.splitext(file)[0]
        l = f.read().split(" ")
        name = Fil + '.JPG'
        img = Image.open(name)
        width = img.width
        height = img.height
        print(l)
        print(height)
        print(width)
        a = l[0]
        x1 =l[1]
        x = int(Decimal(x1)*width)
        y1=l[2]
        y = int(Decimal(y1)*height)
        h1=l[4]
        h =int(Decimal(h1)*height)
        w1=l[3]
        w =int(Decimal(w1)*width)
        print(x,y,w,h)
        img = cv2.imread(name)
        crop_img = img[y-(h//2):y+(h//2), x-(w//2):x+(w//2)]
        #crop_img = cv2.resize(crop_img,(100,100))
        #cv2.imshow("cropped", crop_img)
        #cv2.waitKey(0)
        cv2.imwrite("E:/BE_PROJECT/Cropped_Labelled_Images/" + name , crop_img)
        print(Fil)
        
  
  
# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith(".txt"):
        file_path = f"{path}\{file}"
  
        # call read text file function
        read_text_file(file_path)