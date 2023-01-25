from functional import *
import numpy as np
from M_net import M_net

"""
    learning the provided training data: "PA-D-train.dat"
"""
def learn_training_data():
    """
        load training data
    """
    train = load_training_data_from_file("PA-D-training_data", dtype=float, nopath=True)
    train_arr = train_to_ndarray(train)
    train_shuffle = np.copy(train_arr)
    """
        load specifications of the net
    """
    param = load_specifications(lineNr=1)
    for k,v in param.items():
        print(k,v)
    print()
    """
        draw centers: random subset of training data
    """
    rand_ind = np.random.choice(a=range(len(train_arr)), size=param["K"], replace=False)
    centers = train_arr[rand_ind]
    """
        build exponentially decaying learning rate function
    """
    lr_func = exp_decay_lr(param["init_lr"],param["finish_lr"], len(train))

    net = M_net(param,lr_func,centers)

    """
        training loop
    """
    centers_before = np.copy(net.centers)
    for i in range(param["epoches"]):
        """
            random shuffling of training data
        """
        print("epoch: ",i+1)
        np.random.shuffle(train_shuffle)
        iter = 0
        for sample in train_shuffle:
            net.train(sample,iter)
        iter += 1

    plot_data(train_arr,centers_before,net.centers,param["M"], int(param["K"]/param["M"]))

    centers_to_file("PA-D.net",net.centers)

"""
    learning the demonstartion example; 3 non overlapping areas in the unit cube: 
        for all areas: x1,x2 all values 
            A1: 0<x3<=0.2
            A2: 0.4<=x3<=0.6
            A3: 0.8<=x3<=1
    training data is randomly created
    centers are safed in: "othercenters.net"
"""
def working_properly():
    """
            load training data
    """
    train_arr = load_training_data([0.2,0.4,0.6,0.8], amount=1000, dim=3)
    train_arr = train_to_ndarray(train_arr)
    train_shuffle = np.copy(train_arr)
    """
        load specifications of the net
    """
    param = load_specifications(lineNr=3)
    for k, v in param.items():
        print(k, v)
    print()
    """
        draw centers: random subset of training data
    """
    rand_ind = np.random.choice(a=range(len(train_arr)), size=param["K"], replace=False)
    centers = train_arr[rand_ind]
    """
        build exponentially decaying learning rate function
    """
    lr_func = exp_decay_lr(param["init_lr"], param["finish_lr"], len(train_arr))

    net = M_net(param, lr_func, centers)

    """
        training loop
    """
    for i in range(param["epoches"]):
        """
            random shuffling of training data
        """
        print("epoch: ", i + 1)
        np.random.shuffle(train_shuffle)
        iter = 0
        for sample in train_shuffle:
            net.train(sample, iter)
        iter += 1

    centers_to_file("othercenters-training_data",train_arr)
    centers_to_file("othercenters.net", net.centers)
    do_3d_plot(train_arr,net.centers,param["M"], int(param["K"]/param["M"]))


np.random.seed()

learn_training_data()
working_properly()




