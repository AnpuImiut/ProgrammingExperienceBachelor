

"""
    Implementation of a multilayer perceptron using the standard delta rule for learning.
    Allowed transfer functions are identity, sigmoid and tanh. By task restriction the perceptron
    only supports up to 2 hidden layers(maximal a 4 layer perceptron: input layer, hidden layer #1,
    hidden layer #2 and output layer
"""

import numpy as np
from transfer_functions import *

class MLP:
    def __init__(self,dim,trans_funcs,der_trans_func,lrates):
        """
            restrict the number of layers of the MLP
        """
        cut = 4
        dim = dim[:cut]
        trans_funcs = trans_funcs[:cut]
        lrates = lrates[:cut]
        der_trans_func = der_trans_func[:cut]
        self.__handling_restrictions(dim,trans_funcs,der_trans_func,lrates)
        """
            initialize and prepare the data structures
        """
        self.dimensions = dim
        self.transfer_funcs = [np.vectorize(x) for x in trans_funcs]
        self.der_transfer_funcs = [np.vectorize(x) for x in der_trans_func]
        self.learn_rates = lrates
        self.weight_matrices = []
        self.__create_weight_matrices()
        self.outputs = []
        self.outputs = self.__create_output_matrix(self.outputs)
        """
            saving the net values is helpful for the delta rule
        """
        self.nets = []
        self.nets = self.__create_output_matrix(self.nets)
    def train(self,patterns):
        """
        The training method is single step training with delta rule. So the weight updates happens for each pattern

        :param patterns: vector of patter, each pattern is a 2-element tuple of input array and teacher array
        :return: sum of error for each pattern with error= squared difference of teacher and prediction
        """

        error = 0
        for p in patterns:
            inp, teacher = p[0],p[1]
            self.propagate(inp)
            """ compute delta values for output layer"""
            delta_old = self.__delta_vals_output_layer(teacher, self.get_output(), len(self.der_transfer_funcs)-1)
            delta_new = np.copy(delta_old)
            for i in reversed(range(len(self.weight_matrices))):
                """ 
                compute delta values of the layer above; preparement for the weight update in next iteration.
                For i = 0 it would compute the delta values of the input layer. But in our MLP model there is no
                weight update for input layer.
                """
                if i > 0:
                    delta_new = np.dot(np.transpose(self.weight_matrices[i][:,1:]), delta_old) * self.der_transfer_funcs[i](self.nets[i][1:])
                """ vectorized implementation of the weight update with respect to delta rule """
                self.weight_matrices[i] += self.learn_rates[i] * np.outer(delta_old, self.outputs[i])
                delta_old = np.copy(delta_new)
            error += self.error(teacher, self.get_output())
        return error
    def comparison_test_data(self, patterns):
        for pattern in patterns:
            inp, teacher = pattern[0], pattern[1]
            self.propagate(inp)
            print(teacher, self.get_output())
    def propagate(self,pattern):
        if len(pattern) != self.dimensions[0]:
            raise ValueError("pattern input dimension", len(pattern),"doesnt equals input layer dimension", self.dimensions[0])
        self.outputs[0][1:] = pattern
        self.__propagate()
    def __propagate(self):
        self.nets[0][1:] = self.outputs[0][1:]
        self.outputs[0][1:] = self.transfer_funcs[0](self.outputs[0][1:])
        for i in range(1,len(self.dimensions)):
            self.nets[i][1:] = np.dot(self.weight_matrices[i-1], self.outputs[i-1])
            self.outputs[i][1:] = self.transfer_funcs[i](self.nets[i][1:])
    def __create_weight_matrices(self):
        """
            weight_matrices shall be initialized with random values in [-2,2). [-2,2] is desired,
            but not supported by random generators.
        """
        for i in range(len(self.dimensions)-1):
            """
                The created matrix will be a H-(M+1) matrix where M is the layer before H:
                ...-M-H-...
            """
            tmp = np.random.rand(self.dimensions[i+1], self.dimensions[i]+1)
            tmp = tmp * 4 - 2
            self.weight_matrices.append(tmp)
    def __create_output_matrix(self,matrix):
        for i in range(len(self.dimensions)):
            tmp = np.zeros(self.dimensions[i])
            tmp = np.insert(tmp,0,1)
            matrix.append(tmp)
        return matrix
    def __handling_restrictions(self,dim,transfer_funcs,der_transfunc,learnrates):
        if not (len(dim) == len(transfer_funcs) == len(learnrates)+1 == len(der_transfunc)):
            raise ValueError("Dimension restrictions are not satisfied.\n"
                             "Numbers of layers, of transfer functions per layer and of learnrates must be equal.\n"
                             "Also only up to 2 hidden layers(4 layer perceptron)",
                             len(dim),"==", len(transfer_funcs), "==" ,len(learnrates)+1 ,"==", len(der_transfunc))
        if transfer_funcs[0] != trans_func_ident:
            raise ValueError("\nFirst argument of transfer function vector must be the identity function")
    def get_output(self):
        return self.outputs[len(self.outputs)-1][1:]
    def __delta_vals_output_layer(self,teacher, predictions, layer):
        return (teacher - predictions) * self.der_transfer_funcs[layer](self.nets[layer][1:])
    def error(self,teacher,predictions):
        return 0.5 * np.sum((teacher - predictions)**2)

