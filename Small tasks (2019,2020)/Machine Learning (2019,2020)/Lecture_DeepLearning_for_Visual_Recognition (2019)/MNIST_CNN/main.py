"""
    force cpu
"""
from load_mnist import *
from keras.utils import to_categorical
from net import *
from keras.optimizers import *
from keras.regularizers import *
from keras.datasets import cifar10


#initialize random seed
np.random.seed()

def CNN_learn_MNIST():
    print("loading")
    # Load data - ALL CLASSES
    X_train, y_train = load_mnist('training')
    X_test, y_test = load_mnist('testing')

    print(X_train.shape)
    print("reshaping")
    # Reshape the image data into rows

    x_train = X_train.reshape(X_train.shape + (1,))
    x_test = X_test.reshape(X_test.shape + (1,))
    # Change to float datatype
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    # Scale the data to lie between 0 to 1
    x_train /= 255
    x_test /= 255

    num_classes = 10

    # Change the labels from integer to categorical data
    y_train_one_hot = to_categorical(y_train, num_classes)
    y_test_one_hot = to_categorical(y_test, num_classes)


    layers = [16,32,64]
    image_vector_size = (28, 28, 1)
    print("preparing parameters")
    param = {}
    param["stride"] = [(1, 1),(1,1)]
    param["kernel_s"] = [3,3]
    param["max_stride"] = [(2, 2),(2,2)]
    param["max_pool_s"] = [(2, 2),(2,2)]
    print("creating model")
    reg = l2(0.000)
    model = create_CNN(layers, image_vector_size, num_classes,param,reg,dropout=True)

    print("start training")
    optim = Adam(learning_rate= 0.005)
    lossf = 'categorical_crossentropy'
    evaluate(model, x_train, y_train_one_hot, x_test, y_test_one_hot,
             batch_size=256, epochs=10, opt=optim,loss=lossf)

def CNN_learn_CIFAR10():
    print("loading")
    x = cifar10.load_data()
    x_train,y_train,x_test,y_test = x[0][0],x[0][1],x[1][0],x[1][1]

    # Change to float datatype
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')

    # Scale the data to lie between 0 to 1
    x_train /= 255
    x_test /= 255

    num_classes = 10

    # Change the labels from integer to categorical data
    y_train_one_hot = to_categorical(y_train, num_classes)
    y_test_one_hot = to_categorical(y_test, num_classes)

    layers = [64, 128, 256]
    image_vector_size = (32, 32, 3)
    print("preparing parameters")
    param = {}
    param["stride"] = [(1, 1), (1, 1)]
    param["kernel_s"] = [5, 3]
    param["max_stride"] = [(2, 2), (2, 2)]
    param["max_pool_s"] = [(2, 2), (2, 2)]
    print("creating model")
    reg = l2(0.000)
    model = create_CNN(layers, image_vector_size, num_classes, param, reg, dropout=True)

    print("start training")
    optim = Nadam(learning_rate=0.001)
    lossf = 'categorical_crossentropy'
    evaluate(model, x_train, y_train_one_hot, x_test, y_test_one_hot,
             batch_size=256, epochs=20, opt=optim, loss=lossf)

CNN_learn_MNIST()
CNN_learn_CIFAR10()
