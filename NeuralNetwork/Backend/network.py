# Zain Syed, May 18th 2024
# Project TOOFAN: made for HawkHacks 2024

# Credits to Computer vision engineer on YouTube, his tutorial served as a baseline for this project
# https://www.youtube.com/watch?v=il8dMDlXrIE

#Image dataset from Kaggle: https://www.kaggle.com/datasets/kmader/satellite-images-of-hurricane-damage/data
#Sourced from: http://dx.doi.org/10.21227/sdad-1e56

# This code is a neural network I am creating to help determine safe zones and dangerous areas in a disaster zone

import os
import numpy as np
import pickle

from skimage.io import imread
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

metadataPath = 'C:/Users/zainy/Downloads/TurkeyDamage'

categories = ['damaged', 'undamaged']

data = []
labels = []

for i, category in enumerate(categories):
    for file in os.listdir(os.path.join(metadataPath, category)):
        imgPath = os.path.join(metadataPath, category, file)
        img = imread(imgPath)
        img = resize(img, (15, 15))
        data.append(img.flatten()) # Simplifying the data in order to read it as a 1D value instead of a 2D image

        labels.append(i)

data = np.asarray(data)
labels = np.asarray(labels)

x_train, x_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, shuffle = True ,stratify=labels)

classifier = SVC()
params = [{'gamma': [0.01, 0.001, 0.0001] , 'C': [1, 10, 100, 1000] }]

gridSearch = GridSearchCV(classifier, params)
gridSearch.fit(x_train, y_train)

bestClassifier = gridSearch.best_estimator_

yPrediction = bestClassifier.predict(x_test)

score = (accuracy_score(yPrediction, y_test)) * 100

print('{}% of samples were classified correctly'.format(str(score)))

pickle.dump(bestClassifier, open('./model.p', 'wb'))