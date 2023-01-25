from matplotlib import pyplot as plt
import numpy as np
#need for the 3d plot
from mpl_toolkits.mplot3d import Axes3D

def load_training_data_from_file(filename,dtype,nopath = False):
    if not nopath:
        ans = input("training data should be in same folder. Continue?:Yes(Y), No(N):")
    else:
        ans = 'Y'
    data = []
    if ans == 'Y':
        with open(filename, mode='r') as f:
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
                line = line[:training_data_N]
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

def train_to_ndarray(data):
    ans = np.empty(shape=(data[0].shape))
    for point in data:
        ans = np.vstack((ans,point))
    return ans[1:]

def load_specifications(lineNr):
    with open("specifications",mode='r') as f:
        while True:
            line = f.readline()
            if line[0] != '#':
                break
        if lineNr > 1:
            for i in range(lineNr-2):
                line = f.readline()
            line = f.readline()
        ans = convert_to_dict(line)
        return ans

def convert_to_dict(data):
    data = list(map(float, data.split()))
    for i in range(5):
        data[i] = int(data[i])
    for i in range(data[4]):
        data[4+i+1] = int(data[4+i+1])
    dic = {}
    dic["N"] = data[0]
    dic["M"] = data[1]
    dic["S"] = data[2]
    dic["K"] = data[3]
    dic["G"] = data[4]
    dic["G_dim"] = data[4+1:4+dic["G"]+1]
    dic["gaus-SOM"] = data[len(data)-5]
    dic["gaus-NGas"] = data[len(data)-4]
    dic["init_lr"] = data[len(data)-3]
    dic["finish_lr"] = data[len(data)-2]
    dic["epoches"] = int(data[len(data)-1])
    return dic

class exp_decay_lr():
    def __init__(self,init,finish,max_steps):
        self.init = init
        self.finish = finish
        self.max_steps =max_steps
    def value_at(self,t):
        return self.init * ((self.finish / self.init) ** (t / self.max_steps))

def plot_data(train,centers_before,centers_after,number_nets,neurons_per_net):
    m = 4
    sub = 4
    plt.title("training points and centers distribution before training")
    plt.subplot(1,2,1)
    plt.plot(train[:,0],train[:,1],'ko',label="training points",ms=m)
    for i in range(number_nets):
        plt.plot(centers_before[i*neurons_per_net:(i+1)*neurons_per_net,0],
                 centers_before[i*neurons_per_net:(i+1)*neurons_per_net,1],'o',label="center points",ms=m+sub)
    plt.subplot(1,2,2)
    plt.plot(train[:, 0], train[:, 1], 'ko', label="training points",ms=m)
    for i in range(number_nets):
        plt.plot(centers_after[i * neurons_per_net:(i + 1) * neurons_per_net, 0],
                 centers_after[i * neurons_per_net:(i + 1) * neurons_per_net, 1], 'o', label="center points",ms=m+sub)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

def centers_to_file(filename,centers):
    with open(filename,mode="w") as f:
        for center in centers:
            print(center)
            f.write(str(center)+"\n")

"""
    always assume that dims correspond the last dimension
    luckily there are some theoretical foundations which proof
    that random drawing works fast enough to create sample data
"""
def load_training_data(thresholds,amount=0,dim=0):
    train = []
    for i in range(amount):
        while True:
            tmp = np.random.random(dim)
            tmp_len = len(tmp) - 1
            if tmp[tmp_len] <= thresholds[0]:
                break
            elif tmp[tmp_len] >= thresholds[len(thresholds)-1]:
                break
            found = False
            for i in range(1,len(thresholds)-1,2):
                if thresholds[i] <= tmp[tmp_len] <= thresholds[i+1]:
                    found = True
                    break
            if found:
                break
        train.append(tmp)
    return train

def do_3d_plot(train,centers,number_nets,neurons_per_net):
    s = 8
    ax = plt.axes(projection='3d')
    trainX = train[:,0]
    trainY = train[:,1]
    trainZ = train[:,2]
    centersX = centers[:,0]
    centersY = centers[:,1]
    centersZ = centers[:,2]
    ax.scatter(trainX, trainY, trainZ,label="training points",color='k',s=s)
    for i in range(number_nets):
        ax.scatter(centersX[i*neurons_per_net:(i+1)*neurons_per_net],
                   centersY[i*neurons_per_net:(i+1)*neurons_per_net],
                   centersZ[i*neurons_per_net:(i+1)*neurons_per_net],label="center points",s=s*s)
    plt.legend(loc='best')
    plt.tight_layout()
    plt.show()

