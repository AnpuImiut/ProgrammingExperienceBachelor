from matplotlib import pyplot as plt
from keras.layers import *  # Dense layers are "fully connected" layers
from keras.models import Sequential  # Documentation: https://keras.io/models/sequential/
from time import time


def create_CNN(layer_sizes, image_size, num_classes,param,regularizer,dropout=False,dropout_threshold=0.5):
    model = Sequential()

    stride = param["stride"]
    kernel_s = param["kernel_s"]
    max_stride = param["max_stride"]
    max_pool_s = param["max_pool_s"]
    model.add(Conv2D(filters=layer_sizes[0],
                     kernel_size=kernel_s[0],
                     activation='relu',
                     strides=stride[0],
                     activity_regularizer=regularizer,
                     input_shape=image_size
                     ))
    model.add(MaxPooling2D(pool_size=max_pool_s[0],
                           strides=max_stride[0]
                           ))
    model.add(Conv2D(filters=layer_sizes[1],
                     kernel_size=kernel_s[1],
                     activation='relu',
                     strides=stride[1],
                     activity_regularizer=regularizer
                     ))
    model.add(MaxPooling2D(pool_size=max_pool_s[1],
                           strides=max_stride[1]
                           ))
    model.add(Flatten())
    model.add(Dense(layer_sizes[2], activation='relu'))
    if dropout:
        model.add(Dropout(dropout_threshold))
    model.add(Dense(num_classes, activation='softmax'))
    return model


def evaluate(model, x_train, y_train, x_test, y_test, opt, loss,batch_size=256, epochs=20 ):
    model.summary()

    model.compile(optimizer=opt, loss=loss, metrics=['accuracy'])

    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)
    print("before training")
    print(f'Test loss: {loss:.3}')
    print(f'Test accuracy: {accuracy:.3}')

    t1 = time()
    history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, verbose=2,
                        validation_data=(x_test, y_test))
    t2 = time()
    loss, accuracy = model.evaluate(x_test, y_test, verbose=0)


    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.title('model training loss')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['training', 'validation'], loc='best')

    print("after training")
    print(f'Test loss: {loss:.3}')
    print(f'Test accuracy: {accuracy:.3}')
    print("executed time: ", t2-t1, " sec")
    plt.show()

