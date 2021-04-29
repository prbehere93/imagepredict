from django.shortcuts import render
from .forms import ImageForm
from tensorflow import keras
import cv2
import numpy as np
import os
from django.conf import settings
import io

# Create your views here.
def home(request):
    prediction="None"
    if request.method=='POST':
        model = keras.models.load_model(os.path.join(settings.ML_MODEL_DIR,'model.h5'))
        form=ImageForm(request.POST,request.FILES)
        if form.is_valid():
            img=request.FILES['docfile'].read() #the uploaded files are a class called InMemoryUploadedFile
            img = cv2.imdecode(np.fromstring(img, np.uint8), cv2.IMREAD_COLOR) #converting to a np array
            im = np.expand_dims(img, axis=0)
            im=(im - im.mean()) / im.std() #image preprocessing
            a=model.predict_classes(im)
            prediction=int(a[0][0])
            #print(prediction)
    else:
        form=ImageForm()
    context={'form':form, 'prediction':prediction}
    return render(request,'predict/home.html',context)
