import numpy as np
import math

"""
    'virtual' class for SOM and N-Gas
"""
class base_net:
    def __init__(self,K,C,lr,N):
        self.numberNeurons = K
        self.centers = C
        self.lr_func = lr
        self.winner = None
        self.input_dim = N
    def determine_winner(self,inp):
        return 0
    def train(self,inp,t):
        return
    def gaussian(self,x,s):
        return math.exp(-(x*x)/(2*s))
    def dist(self,i,j):
        return 0
    def h_neighbor(self,i,j,t):
        return 0

class SOM(base_net):
    def __init__(self,K=0,C=[],lr=0, N=0, g=[], gsize=1):
        super().__init__(K,C,lr,N)
        self.grid = g
        self.gaussian_size = gsize
        self.centers_grid_vals = self.create_grid()
    def create_grid(self):
        """
            works like binary counting from 0 and increasing
            this one start with 1
        """
        grid_size = len(self.grid)
        ans = []
        counter = np.ones(grid_size)
        runner = 0
        for center in self.centers:
            ans.append(np.copy(counter))
            if np.array_equal(center, self.centers[len(self.centers)-1]):
                break
            while True:
                counter[runner] += 1
                if counter[runner] > self.grid[runner]:
                    counter[runner] = 1
                    runner += 1
                else:
                    runner = 0
                    break
        return ans
    def determine_winner(self,inp):
        distances = [np.linalg.norm(c-inp) for c in self.centers]
        self.winner = distances.index(min(distances))
        return distances[self.winner]
    def train(self,inp,t):
        for ind in range(len(self.centers)):
            self.centers[ind] += self.lr_func.value_at(t) * self.h_neighbor(self.winner, ind,t) * (inp-self.centers[ind])
    def dist(self, i, j):
        return np.linalg.norm(self.centers_grid_vals[i] - self.centers_grid_vals[j])
    def h_neighbor(self, i, j, t):
        return self.gaussian(self.dist(i,j), self.gaussian_size)

class NGas(base_net):
    def __init__(self):
        pass

