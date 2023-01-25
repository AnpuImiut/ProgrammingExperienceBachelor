import math
import numpy as np
from matplotlib import pyplot as plt

def trans_func_tanh(x):
    return math.tanh(x)
def der_trans_func_tanh(x):
    return 1.0 - trans_func_tanh(x)**2
def trans_func_sigmoid(x):
    return math.exp(x)/(1+math.exp(x))
def der_trans_func_sigmoid(x):
    return trans_func_sigmoid(x)*(1-trans_func_sigmoid(x))
def trans_func_ident(x):
    return x
def der_trans_func_ident(x):
    return 1

def training_data_from_file(filename,dtype,nopath = False):
    if not nopath:
        ans = input("training data should be in same folder. Continue?:Yes(Y), No(N):")
    else:
        ans = 'Y'
    data = []
    if ans == 'Y':
        with open(filename, mode='r') as f:
            line = None
            while True:
                line = f.readline()
                if line[0] != '#':
                    break
            training_data_N, training_data_M = map(int, line.split())
            # compare if dimension given in data matches fixed dimension in percepton
            for line in f:
                # converting line of strings into array of ints
                line = list(map(dtype, line.split()))
                line = np.asarray(line)
                line = [line[:training_data_N],line[training_data_N:]]
                # insert the example in intern data variable
                data.append(line)
            return data
    else:
        return data

def plot(X,Y,title,xlabel,ylabel,filename):
    plt.plot(X,Y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.savefig(filename)
    plt.close()
