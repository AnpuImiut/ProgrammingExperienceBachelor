# -*- coding: utf-8 -*-
"""
Created on  

@author: fame
"""

import numpy as np
import math
 

def predict(X,W,b):  
    """
    implement the function h(x, W, b) here  
    X: N-by-D array of training data 
    W: D dimensional array of weights
    b: scalar bias

    Should return a N dimensional array  
    """

    vec_sig = np.vectorize(sigmoid)
    return vec_sig(np.dot(X, W) + b)
    
 
def sigmoid(a): 
    """
    implement the sigmoid here
    a: N dimensional numpy array

    Should return a N dimensional array  
    """

    return math.exp(a) / (1 + math.exp(a))

def l2loss(X,y,W,b):  
    """
    implement the L2 loss function
    X: N-by-D array of training data 
    y: N dimensional numpy array of labels
    W: D dimensional array of weights
    b: scalar bias

    Should return three variables: (i) the l2 loss: scalar, (ii) the gradient with respect to W, (iii) the gradient with respect to b
     """

    predictions = predict(X,W,b)
    Loss = y - predictions
    Loss_tmp = Loss *  predictions * (1-predictions)
    Loss_w = -2 * np.dot(Loss_tmp,X)
    Loss_b = -2 * np.sum(Loss_tmp)
    Loss = np.sum(Loss)
    return Loss, Loss_w, Loss_b


def train(X,y,W,b, num_iters=1000, eta=0.001):  
    """
    implement the gradient descent here
    X: N-by-D array of training data 
    y: N dimensional numpy array of labels
    W: D dimensional array of weights
    b: scalar bias
    num_iters: (optional) number of steps to take when optimizing
    eta: (optional)  the stepsize for the gradient descent

    Should return the final values of W and b, also returns the change of loss over time
     """

    Loss_vals = np.zeros(1000)
    for i in range(num_iters):
        Loss_vals[i], change_w,change_b = l2loss(X,y,W,b)
        W += -eta * change_w
        b += -eta * change_b
    return W,b,Loss_vals
 