from load_mnist import *
import numpy as np
from keras.utils import to_categorical
from helper import *

#initialize random seed
np.random.seed()

print("loading")
# Load data - ALL CLASSES
X_train, y_train = load_mnist('training')
X_test, y_test = load_mnist('testing')

print("reshaping")
# Reshape the image data into rows
image_vector_size = 28*28
x_train = X_train.reshape(X_train.shape[0], image_vector_size)
x_test = X_test.reshape(X_test.shape[0], image_vector_size)
# Change to float datatype
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

#show_images(x_train)
# Scale the data to lie between 0 to 1
x_train /= 255
x_test /= 255

num_classes = 10

# Change the labels from integer to categorical data
y_train_one_hot = to_categorical(y_train,num_classes)
y_test_one_hot = to_categorical(y_test,num_classes)

layers = 2
#for layers in range(1, 5):
model = create_dense([32] * layers,image_vector_size,num_classes)
evaluate(model, x_train, y_train_one_hot, x_test, y_test_one_hot,batch_size=128,epochs=20)