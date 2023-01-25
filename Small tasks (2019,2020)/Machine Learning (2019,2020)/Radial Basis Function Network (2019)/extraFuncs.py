import numpy as np
from matplotlib import pyplot as plt
import math

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

def plot(X,Y,title,xlabel,ylabel,filename,close=True,save=True, label = None):
    plt.plot(X,Y,label=label)
    if close:
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.legend(loc='best')
        if save:
            plt.savefig(filename)
            plt.close()

""" 
    Function for the regression task. x is bounded in [0,40] and y in [0,150]
"""
def teacher_func(x):
    return 0.02 * x * x * x - 1.06 * x * x + 15 * x
def generate_data(amount,kind):
    for i in range(amount):
        tmp = np.random.rand(amount)*40
        tmp_func = [teacher_func(x) for x in tmp]
        with open(kind+"_data",mode='w') as f:
            for x,y in zip(tmp,tmp_func):
                f.write(str(x) + " " + str(y) + "\n")

def gauß(x,mean,var):
    return math.exp(-(x-mean)**2/(2*var**2))