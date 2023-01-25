from load_mnist import *
from helper import *
import numpy as np
import keras
from keras import backend as K

K.tensorflow_backend._get_available_gpus()
# load data
data = np.load('ORL_faces.npz')
x_train = data['trainX']
y_train = data['trainY']
x_test = data['testX']
y_test = data['testY']
 
image_size = 92*112
x_train = x_train.reshape(x_train.shape[0], image_size)
x_test = x_test.reshape(x_test.shape[0], image_size)
# Change to float datatype
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

# Scale the data to lie between 0 to 1
x_train /= 255
x_test /= 255

num_classes = 20
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

layers = 2
#for layers in range(1, 5):
model = create_dense([32] * layers,image_size,num_classes)
evaluate(model, x_train, y_train, x_test, y_test,batch_size=10,epochs=100)

 