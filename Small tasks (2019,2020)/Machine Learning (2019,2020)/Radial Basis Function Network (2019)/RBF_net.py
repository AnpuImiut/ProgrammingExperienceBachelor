import numpy as np
from scipy import spatial
from scipy import ndimage
import extraFuncs
import math

class RBF:
    def __init__(self,dim,cent,rate):
        self.dimension = dim
        self.centers = np.reshape(cent,(len(cent),1))
        self.learning_rate = rate
        self.weights_mat = []
        self.output_mat = []
        self.dist_mat = []
        self.generate_weights()
        self.gauß_vec = np.vectorize(extraFuncs.gauß)

    def generate_weights(self):
        # MxK mat
        self.weights_mat= (np.random.rand(self.dimension[2],self.dimension[1])) - 0.5

    def compute_distance(self,input_mat):
        # KxP mat
        self.dist_mat = spatial.distance.cdist(self.centers,input_mat,'euclidean')
        # KxP mat
        self.r_mat = self.gauß_vec(self.dist_mat,0,1)
        # MxP mat
        self.output_mat = np.dot(self.weights_mat, self.r_mat)

    def learn_weights(self,patterns, batchsize = 1,learn=True):
        """
         Let P>K: Using the MPPI
         gradient descent be used for training the weights.
         """
        # after this step we have all outputs(hidden+final) on all patterns saved in class variables
        inp, teacher = [],[]
        for p in patterns:
            inp.append(p[0])
            teacher.append(p[1])
        inp = np.asarray(inp)
        teacher = np.asarray(teacher)
        self.compute_distance(inp)
        if learn:
            for i in range(len(patterns)):
                if i+1 % batchsize == 0:
                    tmp = self.weight_change(i+1,batchsize,teacher)
                    self.weights_mat += tmp
                elif batchsize==1:
                    tmp = self.weight_change(i + 1, batchsize, teacher)
                    self.weights_mat += tmp
        return self.error(inp,teacher)
    def weight_change(self,index,batchsize,teacher):
        A = teacher[index-batchsize:index] - self.output_mat[:,index-batchsize:index]
        B = np.transpose(self.r_mat)[index-batchsize:index,:]
        delta_w = np.dot(A,B)
        return delta_w * self.learning_rate
    def error(self,inp,teacher):
        """
            computes error on all pattern and returns the value
        """
        self.compute_distance(inp)
        error = 0
        for t,prediction in zip(teacher,np.transpose(self.output_mat)):
            tmp = t - prediction
            tmp *= tmp
            error += np.sum(tmp)
        return math.log(error)
    def get_predictions(self):
        return np.transpose(self.output_mat)

    """
    case Interpolation P=K
    To calculate the weights first the number of patterns and RBF neurons be checked.
    Correspond to the result the weights be calculated.
    """
    def interpolate_weights(self, patterns):
        self.weights_matrix = np.zeros(len(self.r_mat), len(self.output_mat))
        if(len(self.r_mat)==len(patterns)):
            self.weights_matrix = np.dot(np.linalg.inv(self.r_mat),self.output_mat)
        elif(len(self.r_mat)>len(patterns)):
            r_plus_mat = np.dot(np.linalg.inv(np.dot(np.transpose(self.r_mat),self.r_mat)),np.transpose(self.r_mat))
            self.weight_matrix = np.dot(r_plus_mat,self.output_mat)
        else:
            pass





