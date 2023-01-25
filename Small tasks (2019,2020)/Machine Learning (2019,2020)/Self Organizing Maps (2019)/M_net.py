from nets import *

"""
    This is meant to contain both: SOM and N-Gas
"""
class M_net:
    """
        assumptions: Partner SOMs, Partner N-Gases
        M:= number of nets, S:= number of SOM nets -> M-S:= number of N-Gas,
            N:= input dimension, g:= Grid for SOM, lr:= learning_rate, C := centers
    """
    def __init__(self,param,lr,C):
        self.param = param
        self.numberSOMs = param["S"]
        self.numberNGas = param["M"] - param["S"]
        self.inputdim = param["N"]
        self.neurons_per_net = int(param["K"]/param["M"])
        self.grid = param["G_dim"]
        self.lr_func = lr
        self.centers = C
        self.nets = self.create_nets()
    def create_nets(self):
        nets = []
        for i in range(self.numberSOMs+self.numberNGas):
            if i < self.numberSOMs:
                # parameters: K = 0, C = [], lr = 0, N = 0, g = [], gsize = 1
                nets.append(SOM(self.neurons_per_net,
                                self.centers[i*self.neurons_per_net:(i+1)*self.neurons_per_net],
                                self.lr_func,
                                self.inputdim,
                                self.grid,
                                self.param["gaus-SOM"]))
            else:
                nets.append(NGas())
        return nets
    def train(self,sample,iteration):
        """
            determine winner net
        """
        winner = self.determine_winner_net(sample)
        """
            train winner net
        """
        self.nets[winner].train(sample,iteration)
    def determine_winner_net(self,input):
        """
            returns the distances not indices
        """
        ans = [self.nets[i].determine_winner(input) for i in range(self.param["M"])]
        return ans.index(min(ans))



