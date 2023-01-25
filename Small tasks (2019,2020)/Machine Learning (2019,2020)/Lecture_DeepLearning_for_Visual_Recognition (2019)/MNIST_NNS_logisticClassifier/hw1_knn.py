# -*- coding: utf-8 -*-
"""
Created on  

@author: fame
"""
 
import numpy as np
from scipy.spatial.distance import cdist
from matplotlib import pyplot as plt
 

def compute_euclidean_distances( X, Y ) :
    """
    Compute the Euclidean distance between two matricess X and Y
    Input:
    X: N-by-D numpy array 
    Y: M-by-D numpy array 
    
    Should return dist: M-by-N numpy array   
    """

    return cdist(Y,X)

def predict_labels(dists, labels, k=1):
    """
    Given a Euclidean distance matrix and associated training labels predict a label for each test point.
    Input:
    dists: M-by-N numpy array
    labels: is a N dimensional numpy array

    Should return  pred_labels: M dimensional numpy array
    """

    ans = np.zeros(dists.shape[0])
    neighbours = np.zeros(shape=(dists.shape[0],k))
    for row,i in zip(dists,range(dists.shape[0])):
        sorted_row_indices = np.argsort(row)
        neighbours[i] = sorted_row_indices[:k]
        labels_copy = np.copy(labels)
        labels_copy = labels_copy[sorted_row_indices]
        labels_copy = labels_copy[:k]
        (classes,counts) = np.unique(labels_copy, return_counts=True)
        ans[i] = classes[np.argmax(counts)]
    return ans,neighbours.astype(int)

"""
    Will use resevoir sampling to generate the indices for the sample training data. The main problem is
    that we cant draw 100 random samples for each class by normal methodes because we dont know beforehand 
    which rows are associated with which class. Resevoir sampling bypass this because we just can count
    for each class how many occurences we have and build our random sample while iterating over whole training data
"""
def sampling_multiple_classes(data,nmbr_classes,samplesize):
    samplesize_per_class = samplesize//nmbr_classes
    data_list = data.tolist()
    #first column = number of class items found
    sample = np.zeros(shape=(nmbr_classes,samplesize_per_class+1),dtype=int)
    for element,index in zip(data,range(len(data))):
        if sample[element-1][0] < samplesize_per_class:
            sample[element-1][int(sample[element-1][0]+1)] = index
            sample[element - 1][0] += 1
        else:
            rnd_int = np.random.randint(1,sample[element-1][0]+1)
            sample[element-1][0] += 1
            if rnd_int <= samplesize_per_class:
                sample[element-1][rnd_int] = index
    sample = sample[:,1:]
    return sample.flatten()


def visualizer_knn(test_data,training_data,sorting,amount,k):
    f, axxar = plt.subplots(amount,k+1)
    for i in range(amount):
        axxar[i][0].imshow(test_data[i])
        k_nearest = training_data[sorting[i]]
        for j in range(1,k+1):
            axxar[i][j].imshow(k_nearest[j-1])
    plt.show()