import torch.nn as tnn
import torch
import numpy as np
from torch.utils.data import Dataset,DataLoader

class MLP(tnn.Module):
    def __init__(self,dim,device,l1alpha=0):
        super(MLP,self).__init__()
        self.layers = tnn.Sequential(*self.build_layers(dim))
        self.device = device
        self.l1alpha = torch.tensor(l1alpha)
        self.l1alpha = self.l1alpha.to(device)
    def forward(self,x):
        x = self.layers(x)
        return x
    def build_layers(self,dim):
        """
            hardcoded layers
        """
        layers = []
        layers.append(tnn.Linear(dim[0],dim[1]))
        layers.append(tnn.ReLU())
        layers.append(tnn.Linear(dim[1],dim[2]))
        layers.append(tnn.ReLU())
        layers.append(tnn.Linear(dim[2],dim[3]))
        return layers
    def train_epoches(self,data,opt,lossfunc,epoches=5,batchsize=1):
        mean_train_losses = []
        mean_test_losses = []
        train_acc_list = []
        test_acc_list = []
        train_loader = DataLoader(dataset=data["train"],batch_size=batchsize,shuffle=True)
        test_loader = DataLoader(dataset=data["test"],batch_size=batchsize//2,shuffle=False)

        for epoch in range(epoches):
            self.train()

            train_losses = []
            test_losses = []
            correct = 0
            total = 0
            for i, (images, labels) in enumerate(train_loader):
                images = images.to(self.device)
                labels = labels.to(self.device)

                opt.zero_grad()

                outputs = self(images)
                outputs = outputs.to(self.device)
                loss = lossfunc(outputs,labels)
                loss = loss.to(self.device)
                loss += self.l1alpha * self.l1_regularization()
                loss.backward()
                opt.step()

                train_losses.append(loss.item())

                _, predicted = torch.max(outputs.data, 1)
                correct += (predicted == labels).sum().item()
                total += labels.size(0)

                if (i * batchsize) % (batchsize * 100) == 0:
                    print(f'{i * batchsize} / {data["train"].x_data.shape[0]}')

            self.eval()
            train_accuracy = 100 * correct / total
            train_acc_list.append(train_accuracy)

            correct = 0
            total = 0
            with torch.no_grad():
                for i, (images, labels) in enumerate(test_loader):
                    images = images.to(self.device)
                    labels = labels.to(self.device)

                    outputs = self(images)
                    outputs = outputs.to(self.device)
                    loss = lossfunc(outputs, labels)
                    loss = loss.to(self.device)

                    test_losses.append(loss.item())

                    _, predicted = torch.max(outputs.data, 1)
                    correct += (predicted == labels).sum().item()
                    total += labels.size(0)

            mean_train_losses.append(np.mean(train_losses))
            mean_test_losses.append(np.mean(test_losses))


            test_accuracy = 100 * correct / total
            test_acc_list.append(test_accuracy)
            print('epoch : {}, train loss : {:.4f}, train acc : {:.2f}%, test loss : {:.4f}, test acc : {:.2f}%' \
                  .format(epoch + 1, np.mean(train_losses), train_accuracy, np.mean(test_losses), test_accuracy))
        dict = {}
        dict["train_loss"] = mean_train_losses
        dict["test_loss"] = mean_test_losses
        dict["train_acc"] = train_acc_list
        dict["test_acc"] = test_acc_list

        return dict
    def l1_regularization(self):
        if self.l1alpha == 0:
            return torch.tensor(0)
        else:
            loss = torch.tensor(0,dtype=float)
            loss = loss.to(self.device)
            for param in self.parameters():
                loss += torch.norm(param, p=1)
            return loss

"""
    easy way to prepare for batch learning. This makes it possible later 
    to use torch functions to implement the batch learning.
"""
class data_set(Dataset):
    def __init__(self,x_data,y_data):
        """
            assumption: data is a multidimensional tensor with each element in the first dimenension being a sample
        """
        self.x_data = x_data
        self.y_data = y_data
        self.len = x_data.shape[0]
    def __getitem__(self, index):
        return self.x_data[index], self.y_data[index]
    def __len__(self):
        return self.len
