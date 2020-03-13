from django.shortcuts import render

from django.http import HttpResponse

from .models import TestImage

from .forms import TestImageForm

import cv2
import tensorflow as tf
import os

# Create your views here.

def prepare(filepath):
    IMG_SIZE = 127
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

def index(request):
    if request.method == 'POST':
        form = TestImageForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()

            lastImage = TestImage.objects.last()
            imagefile = str(lastImage.picture)
            #print(imagefile) #testPictures/Screenshot_from_2020-02-18_21-15-35_s053hvK.png

            CATEGORIES = ['NORMAL', 'PNEUMONIA']
            model = tf.keras.models.load_model('/media/nazmul/DATA/work/onlinePneumoniaClassfication/medicalImageClassifier/imgClassificationApp/pneumonia_1_0.model')

            const_path = '/media/nazmul/DATA/work/onlinePneumoniaClassfication/medicalImageClassifier/media'

            test_img_path = os.path.join(const_path, imagefile)

            prediction = model.predict([prepare(test_img_path)])   #this always takes a list. remember.

            final_classification = str(CATEGORIES[int(prediction[0][0])])

            lastImage.delete()

            return HttpResponse(final_classification)

    else:
        form = TestImageForm()
        return render(request, 'index.html', {'form':form})