# -*- coding: utf-8 -*-
"""
Created on 

@author: fame
"""

 
from load_mnist import * 
import hw1_knn  as mlBasics
import numpy as np
import time
import cProfile

prof = cProfile.Profile()
   
print("loading")
classes = np.arange(10)
# Load data - ALL CLASSES
X_train, y_train = load_mnist('training',classes)
X_test, y_test = load_mnist('testing',classes)

print("reshaping")
 # Reshape the image data into rows  
X_train = np.reshape(X_train, (X_train.shape[0], -1))
X_test = np.reshape(X_test, (X_test.shape[0], -1))


print("calculating distances")
# Test on test data   
#1) Compute distances:
#dists = mlBasics.compute_euclidean_distances(X_train,X_test)

#load either "distance_matrix" for all classes or "distance_matrix_small" for 2 classes
dists = np.fromfile("distance_matrix")
dists = np.reshape(dists,(X_test.shape[0],X_train.shape[0]))

print("predictions")
#2) Run the code below and predict labels:
prof.enable()
y_test_pred, neigbours = mlBasics.predict_labels(dists, y_train,)
prof.disable()

#3) Report results
# you should get following message '99.91 of test examples classified correctly.'
print('{0:0.02f}'.format(np.mean(y_test_pred == y_test)*100), "of test examples classified correctly.")

prof.print_stats()
