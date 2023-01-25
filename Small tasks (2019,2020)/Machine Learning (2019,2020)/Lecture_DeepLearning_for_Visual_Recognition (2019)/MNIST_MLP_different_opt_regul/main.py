import torch.cuda as tcuda
from MLP import *
from helper import *
from torch import nn as tnn
from torch import optim
import time

device = None
if tcuda.is_available():
    print("CUDA device")
    device = torch.device('cuda:0')
else:
    print("CPU device")
    device = torch.device('cpu')

def MLP1(data,dim,batchsize):
    net = MLP(dim,device)
    net = net.to(device)
    opt = optim.SGD(net.parameters(), lr=0.01)
    loss = tnn.CrossEntropyLoss()
    epoches = 25
    """
        results is a dictionary with access: "train_loss","test_loss","train_acc","test_acc"
    """
    results = net.train_epoches(data,opt,loss,epoches,batchsize)
    return results
def MLP2(data,dim,batchsize):
    net = MLP(dim,device)
    net = net.to(device)
    opt = optim.SGD(net.parameters(), lr=0.01, momentum=0.9, nesterov=True)
    loss = tnn.CrossEntropyLoss()
    epoches = 25
    """
        results is a dictionary with access: "train_loss","test_loss","train_acc","test_acc"
    """
    results = net.train_epoches(data,opt,loss,epoches,batchsize)
    return results
def MLP3(data,dim,batchsize):
    net = MLP(dim,device)
    net = net.to(device)
    opt = optim.SGD(net.parameters(), lr=0.01, momentum=0.9, nesterov=True, weight_decay=1e-4)
    loss = tnn.CrossEntropyLoss()
    epoches = 25
    """
        results is a dictionary with access: "train_loss","test_loss","train_acc","test_acc"
    """
    results = net.train_epoches(data,opt,loss,epoches,batchsize)
    return results
def MLP4(data,dim,batchsize):
    net = MLP(dim,device,l1alpha=1e-4)
    net = net.to(device)
    opt = optim.SGD(net.parameters(), lr=0.01, momentum=0.9, nesterov=True)
    loss = tnn.CrossEntropyLoss()
    epoches = 25
    """
        results is a dictionary with access: "train_loss","test_loss","train_acc","test_acc"
    """
    results = net.train_epoches(data,opt,loss,epoches,batchsize)
    return results


"""
    dictionaries: access via 'x_train','x_test','y_train','y_test'
"""
print("loading data")
MNIST_data = load_and_prepare_MNIST()
ORL_data = load_and_prepare_ORL_faces()

print("preparing/converting data")
MNIST_data = numpy_to_tensor_converter(MNIST_data)
ORL_data = numpy_to_tensor_converter(ORL_data)

"""
    from here: access via 'train','test'
    be aware that they are now of class dataset from torch.utils.data.dataset
"""

MNIST_data = tensor_to_torch_dataset_converter(MNIST_data)
ORL_data = tensor_to_torch_dataset_converter(ORL_data)
print("data transformations finished")

neurons_hiLay = list(map(int,input("Enter dimension of hidden layers: ").split()))
MNIST_dim = [784] + neurons_hiLay + [10]
ORL_dim = [10304] + neurons_hiLay + [20]
MNIST_batchsize = int(input("batchsize for MNIST "))
ORL_batchsize = int(input("batchsize for ORL "))
t1 = time.time()
print("first MLP")
MLP1_MNIST_results = MLP1(MNIST_data,MNIST_dim,MNIST_batchsize)
MLP1_ORL_results = MLP1(ORL_data,ORL_dim,ORL_batchsize)
print("second MLP")
MLP2_MNIST_results = MLP2(MNIST_data,MNIST_dim,MNIST_batchsize)
MLP2_ORL_results = MLP2(ORL_data,ORL_dim,ORL_batchsize)
print("third MLP")
MLP3_MNIST_results = MLP3(MNIST_data,MNIST_dim,MNIST_batchsize)
MLP3_ORL_results = MLP3(ORL_data,ORL_dim,ORL_batchsize)
print("fourth MLP")
MLP4_MNIST_results = MLP4(MNIST_data,MNIST_dim,MNIST_batchsize)
MLP4_ORL_results = MLP4(ORL_data,ORL_dim,ORL_batchsize)
t2 = time.time()
print("exection time: ",t2-t1," sec")

plt.plot(MLP1_MNIST_results["test_loss"])
plt.plot(MLP2_MNIST_results["test_loss"])
plt.plot(MLP3_MNIST_results["test_loss"])
plt.plot(MLP4_MNIST_results["test_loss"])
plt.title('model loss test data; MNIST')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(["SGD","NeMo","NeMo+L2","NeMo+L1"], loc='best')
plt.show()


plt.plot(MLP1_MNIST_results["test_acc"])
plt.plot(MLP2_MNIST_results["test_acc"])
plt.plot(MLP3_MNIST_results["test_acc"])
plt.plot(MLP4_MNIST_results["test_acc"])
plt.title('model accuracy on test data; MNIST')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(["SGD","NeMo","NeMo+L2","NeMo+L1"], loc='best')
plt.show()

plt.plot(MLP1_ORL_results["test_loss"])
plt.plot(MLP2_ORL_results["test_loss"])
plt.plot(MLP3_ORL_results["test_loss"])
plt.plot(MLP4_ORL_results["test_loss"])
plt.title('model loss test data; ORL')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(["SGD","NeMo","NeMo+L2","NeMo+L1"], loc='best')
plt.show()


plt.plot(MLP1_ORL_results["test_acc"])
plt.plot(MLP2_ORL_results["test_acc"])
plt.plot(MLP3_ORL_results["test_acc"])
plt.plot(MLP4_ORL_results["test_acc"])
plt.title('model accuracy on test data, ORL')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(["SGD","NeMo","NeMo+L2","NeMo+L1"], loc='best')
plt.show()



