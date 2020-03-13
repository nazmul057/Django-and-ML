import cv2
import tensorflow as tf

CATEGORIES = ['NORMAL', 'PNEUMONIA']

filepath = r'D:\D\pneumonia_datasets\pn.jpeg'

IMG_SIZE = 127
img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
to_be_feed_to_model = new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model('pneumonia_1_0.model')

prediction = model.predict([to_be_fed_to_model])   #this always takes a list. remember.

print(CATEGORIES[int(prediction[0][0])])