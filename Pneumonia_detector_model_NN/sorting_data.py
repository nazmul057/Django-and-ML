import numpy as np   #for array operations
import matplotlib.pyplot as plt  #to show images
import os     # to iterate through directories and join paths
import cv2  #to do some image operations
import random
import pickle


DATADIR =  "D:\D\pneumonia_datasets\chest_xray\P_train"
CATEGORIES = ['NORMAL', 'PNEUMONIA']

'''
for category in CATEGORIES:
    path = os.path.join(DATADIR, category)  #path to cats or dogs
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        #plt.imshow(img_array, cmap = 'gray')
        #plt.show()
        break
    break

#print(img_array.shape)

'''
'''
IMG_SIZE = 50
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  #(IM_SIZE, IM_SIZE) means (x pixel values, y pixel values)
plt.imshow(new_array, cmap = 'gray')
plt.show()

'''

#print(img_array)

IMG_SIZE = 127


training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)  # path to cats or dogs
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))  # (IM_SIZE, IM_SIZE) means (x pixel values, y pixel values)
                training_data.append([new_array, class_num])

            except Exception as e:
                pass


create_training_data()

#print(len(training_data))

random.shuffle(training_data)

#for sample in training_data[:10]:
#    print(sample[1])  # sample[0] are the whole image arrays

X = []
y = []

for features, labels in training_data:
    X.append(features)
    y.append(labels)

X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)  # -1 means any value(we do not know size of features)
                                                    # array is used because neural net do not take lists as inputs
                                                    # the 1 at last is for GRAY_SCALING if no GRAY_SCALING, the it should be 3

pickle_out = open('X.pickle', 'wb')
pickle.dump(X,pickle_out)
pickle_out.close()

pickle_out = open('y.pickle', 'wb')
pickle.dump(y,pickle_out)
pickle_out.close()