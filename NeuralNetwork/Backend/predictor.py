# Zain Syed, May 18th 2024
# Project TOOFAN: made for HawkHacks 2024

# This code is a test of the Neural Network I made in the other file 
#(so far, it has predicted broken and unbroken buildings with 96% accuracy), on top of this, it got 10/10 correct of my manual tests

import pickle
import numpy as np
from skimage.io import imread
from skimage.transform import resize

def loadModel(path):
    with open(path, 'rb') as file:
        model = pickle.load(file)
    return model

def processImage(image_path):
    img = imread(image_path)
    img = resize(img, (15, 15))
    img_flattened = img.flatten()
    return img_flattened

def predict(images, model):
    processed_images = [processImage(image) for image in images]
    predictions = model.predict(processed_images)
    return predictions

model = loadModel('model.p')

# Testing the 10 images I downloaded (5 damaged, 5 undamaged)
imagePaths = [ 'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/1.jpg' , 
               'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/2.jpg' , 
               'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/3.jpg' ,
               'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/4.jpg' , 
               'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/5.jpg' , 
               'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/6.jpg' ,
                'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/7.jpg' , 
                'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/8.jpg' , 
                'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/9.jpg' ,
                'C:/Users/zainy/Downloads/NeuralNetworkWork/NetworkTesters/10.jpg' ]
predictions = predict(imagePaths, model)
categories = ['damaged' if prediction == 0 else 'undamaged' for prediction in predictions]

i = 1
for i, (_,category) in enumerate(zip(imagePaths, categories) , 1):
    print(f'Image {i} is predicted to be: {category}')
    i+=1