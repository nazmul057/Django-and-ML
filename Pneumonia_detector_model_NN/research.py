import numpy as np   #for array operations
import matplotlib.pyplot as plt  #to show images
import os     # to iterate through directories and join paths
import cv2  #to do some image operations
import random
import pickle


DATADIR =  "D:\D\pneumonia_datasets\chest_xray\P_train"
CATEGORIES = ['NORMAL', 'PNEUMONIA']


for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        #plt.imshow(img_array, cmap='gray')
        #plt.show()
        break
    break

print(img_array.shape)

'''
IMG_SIZE = 100
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  #(IM_SIZE, IM_SIZE) means (x pixel values, y pixel values)
plt.imshow(new_array, cmap = 'gray')
plt.show()

'''