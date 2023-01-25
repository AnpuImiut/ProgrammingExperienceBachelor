import perceptron
import numpy as np
from transfer_functions import *


""" Initialize random generator """
np.random.seed()

""" Prepare transfer functions"""
sig = trans_func_sigmoid
id = trans_func_ident
tanh = trans_func_tanh

d_sig = der_trans_func_sigmoid
d_id = der_trans_func_ident
d_tanh = der_trans_func_tanh

def learn_XOR():
    dimensions = [2, 4, 1]
    transfer_funcs = [id] + [sig] + [id]
    der_transfer_funcs = [d_id] + [d_sig] + [d_id]
    learnrates = [0.2,0.02]
    MLP_XOR = perceptron.MLP(dimensions, transfer_funcs, der_transfer_funcs, learnrates)

    training_data = training_data_from_file("train_XOR",float,True)
    Loss = []
    for i in range(1000):
        Loss.append(MLP_XOR.train(training_data))
    MLP_XOR.comparison_test_data(training_data)
    print(min(Loss),end="\n")
    X = range(1,1001)
    title = "MLP: XOR learning curve with \ndim[2,4,1] and transfer functios[id,sig,id]"
    xlabel = "iterations"
    ylabel = "E(Patterns)"
    filenname = "MLP_XOR_learningcurve"
    plot(X,Loss,title,xlabel,ylabel,filenname)

def learn_sample3():
    dimensions = [4,6,4,2]
    transfer_funcs = [id] + 2* [sig] + [id]
    der_transfer_funcs = [d_id] + 2* [d_sig] + [d_id]
    learnrates = [0.2,0.05, 0.02]
    MLP_sample3 = perceptron.MLP(dimensions, transfer_funcs, der_transfer_funcs, learnrates)

    training_data = training_data_from_file("train_sample3", float, True)
    Loss = []
    for i in range(1000):
        Loss.append(MLP_sample3.train(training_data))
    MLP_sample3.comparison_test_data(training_data)
    print(min(Loss),end="\n")

    X = range(1, 1001)
    title = "MLP: train sample 3 learning curve with \ndim[4,6,4,2] and transfer functios[id,sig,sig,id]"
    xlabel = "iterations"
    ylabel = "E(Patterns)"
    filenname = "MLP_trainingsample3_learningcurve"
    plot(X, Loss, title, xlabel, ylabel, filenname)

def learn_sample4():
    dimensions = [2,3, 1]
    transfer_funcs = [id] + [sig] + [id]
    der_transfer_funcs = [d_id] + [d_sig] + [d_id]
    learnrates = [0.2, 0.02]
    MLP_sample4 = perceptron.MLP(dimensions, transfer_funcs, der_transfer_funcs, learnrates)

    training_data = training_data_from_file("train_sample4", float, True)
    Loss = []
    for i in range(1000):
        Loss.append(MLP_sample4.train(training_data))
    MLP_sample4.comparison_test_data(training_data)
    print(min(Loss),end="\n")

    X = range(1, 1001)
    title = "MLP: train sample 4 learning curve with \ndim[2,3,1] and transfer functios[id,sig,id]"
    xlabel = "iterations"
    ylabel = "E(Patterns)"
    filenname = "MLP_trainingsample4_learningcurve"
    plot(X, Loss, title, xlabel, ylabel, filenname)

learn_XOR()
learn_sample3()
learn_sample4()

