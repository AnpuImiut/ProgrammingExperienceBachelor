from load_mnist import *
import hw1_knn  as mlBasics
import numpy as np
import time
import cProfile
from sklearn import metrics
from matplotlib import pyplot as plt



#initialize random seed
np.random.seed()

print("loading")
# Load data - ALL CLASSES
X_train, y_train = load_mnist('training'  )
X_test, y_test = load_mnist('testing'   )

print("reshaping")
 # Reshape the image data into rows
X_train_flatten = np.reshape(X_train, (X_train.shape[0], -1))
X_test_flatten = np.reshape(X_test, (X_test.shape[0], -1))
y_train = y_train.astype(int)

""" TASK b
    random sample will be an array of indices. So we can work on the distance matrix of all 
    training and test points. To get the dist for a set of training points we just transpose 
    matrix and select the correct rows and transpose back. For the visualizing we will use 
    functions from matplotlib.
"""
print("drawing_random_sample")
#get number of classes
nmbr_classes = len(set(y_train))
#draw the indices of the random sample
rnd_indices = mlBasics.sampling_multiple_classes(y_train,nmbr_classes,1000)
sample_X_train = X_train[rnd_indices]
sample_Y_train = y_train[rnd_indices]

""" 
    The computation uses the cdist function from scipy library. Still for whole distance matrix 
    it used me 10 min(Intel i7-7700). So we decided to safe the computation and load is everytime 
    which is way faster.
"""
print("calculating distances")

#1) Compute distances:

#dists = mlBasics.compute_euclidean_distances(sample_X_train_flatten,X_test_flatten)
dists = np.fromfile("distance_matrix")
dists = np.reshape(dists,(X_test.shape[0],X_train.shape[0]))
transpose_dists = np.transpose(dists)

#this code saves the distance matrix as binary file
#dists.tofile("distance_matrix")

print("predictions on sample training data for k=1 and k=5")
sample_dists = transpose_dists[rnd_indices]
sample_dists = np.transpose(sample_dists)
y_test_pred_k1, neighbours_k1 = mlBasics.predict_labels(sample_dists, sample_Y_train)
y_test_pred_k5, neighbours_k5 = mlBasics.predict_labels(sample_dists, sample_Y_train, 5)

#3) Report results

print("k=1; "'{0:0.02f}'.format( np.mean(y_test_pred_k1 == y_test)*100), "of test examples classified correctly.")
print("k=5; "'{0:0.02f}'.format( np.mean(y_test_pred_k5 == y_test)*100), "of test examples classified correctly.")

#4 Visualizes either k = 1 nearest neighbor or k = 5 for the first 10 test images

mlBasics.visualizer_knn(X_test,sample_X_train,neighbours_k1,10,1)
mlBasics.visualizer_knn(X_test,sample_X_train,neighbours_k5,10,5)

#5 confusion matrix

print("confusion matrix for k=1")
print(metrics.confusion_matrix(y_test,y_test_pred_k1))
print("confusion matrix for k=5")
print(metrics.confusion_matrix(y_test,y_test_pred_k5))

""" TASK c
    Straightforward implementation. Slicing makes this task very easy.
"""
#6 5-fold cross validation
print("5-fold cross validations")
np.random.shuffle(rnd_indices)
foldsize = len(sample_X_train)//5
accuracies = np.zeros(shape=15)
for k in range(1,16):
    accuracy = 0
    for i in range(5):
        indices_train, indices_test = np.concatenate((rnd_indices[:i*foldsize],rnd_indices[(i+1)*foldsize:])), rnd_indices[i*foldsize:(i+1)*foldsize]
        tmp_dist = mlBasics.compute_euclidean_distances(X_train_flatten[indices_train],X_train_flatten[indices_test])
        y_test_pred, not_need = mlBasics.predict_labels(tmp_dist,y_train[indices_train], k)
        tmp_acc = np.mean(y_test_pred == y_train[indices_test])
        accuracies[k-1] = tmp_acc

k_crossfold_best = np.argmax(accuracies)
print("best accuracy at:(acc,k) ->",('{0:0.04f}'.format(accuracies[k_crossfold_best]),k_crossfold_best+1))

"""
    This code here visualizes the accuracies as a bar chart graph
"""
objects = np.arange(len(accuracies))
y_pos = np.arange(len(accuracies))

plt.bar(y_pos, accuracies, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('accuracy')
plt.show()

""" TASK d
    Here we can make use that we have already computed the whole distance matrix. 
"""
print("comparison of best k from crossfold with k=1")
t1 = time.time()
y_test_pred, not_need = mlBasics.predict_labels(dists, y_train)
t2 = time.time()

k1_time = t2 -t1
k1_acc = np.mean(y_test_pred == y_test)

t1 = time.time()
y_test_pred, not_need = mlBasics.predict_labels(dists, y_train, k_crossfold_best+1)
t2 = time.time()

k_crossfold_best_time = t2 - t1
k_crossfold_best_acc = np.mean(y_test_pred == y_test)

print("k = 1")
print("(time,acc) ->",(k1_time,k1_acc))
print()
print("k = crossfold_best = ", k_crossfold_best+1)
print("(time,acc) ->",(k_crossfold_best_time,k_crossfold_best_acc))