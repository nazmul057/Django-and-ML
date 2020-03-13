import cv2
import tensorflow as tf

CATEGORIES = ['NORMAL', 'PNEUMONIA']

def prepare(filepath):
    IMG_SIZE = 127
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model('pneumonia_1_0.model')

prediction = model.predict([prepare(r'D:\D\pneumonia_datasets\pn.jpeg')])   #this always takes a list. remember.

print(CATEGORIES[int(prediction[0][0])])