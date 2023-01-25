from loading_data import *
from matplotlib import pyplot as plt
import torch
from MLP import data_set

def load_and_prepare_MNIST():
    # Load data - ALL CLASSES
    X_train, y_train = load_mnist('training')
    X_test, y_test = load_mnist('testing')
    # Reshape the image data into rows
    image_vector_size = 28 * 28
    x_train = X_train.reshape(X_train.shape[0], image_vector_size)
    x_test = X_test.reshape(X_test.shape[0], image_vector_size)
    # Change to float datatype
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    # Scale the data to lie between 0 to 1
    x_train /= 255
    x_test /= 255

    dict = {
        "x_train":x_train,
        "y_train":y_train,
        "x_test":x_test,
        "y_test":y_test
    }
    return dict

def load_and_prepare_ORL_faces():
    # Load data - ALL CLASSES
    x_train, y_train, x_test, y_test = load_ORL_faces()
    # Reshape the image data into rows
    image_size = 92 * 112
    x_train = x_train.reshape(x_train.shape[0], image_size)
    x_test = x_test.reshape(x_test.shape[0], image_size)
    # Change to float datatype
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    # Scale the data to lie between 0 to 1
    x_train /= 255
    x_test /= 255

    dict = {
        "x_train": x_train,
        "y_train": y_train,
        "x_test": x_test,
        "y_test": y_test
    }
    return dict

def show_images(images, cols=1, titles=None):
    """Display a list of images in a single figure with matplotlib.

    Parameters
    ---------
    images: List of np.arrays compatible with plt.imshow.

    cols (Default = 1): Number of columns in figure (number of rows is
                        set to np.ceil(n_images/float(cols))).

    titles: List of titles corresponding to each image. Must have
            the same length as titles.
    """
    assert ((titles is None) or (len(images) == len(titles)))
    n_images = len(images)
    if titles is None: titles = ['Image (%d)' % i for i in range(1, n_images + 1)]
    fig = plt.figure()
    for n, (image, title) in enumerate(zip(images, titles)):
        a = fig.add_subplot(cols, np.ceil(n_images / float(cols)), n + 1)
        if image.ndim == 2:
            plt.gray()
        plt.imshow(image)
        a.set_title(title)
    fig.set_size_inches(np.array(fig.get_size_inches()) * n_images)
    plt.show()

def numpy_to_tensor_converter(data):
    data["x_train"] = torch.tensor(data["x_train"])
    data["y_train"] = torch.tensor(data["y_train"],dtype=torch.long)
    data["x_test"] = torch.tensor(data["x_test"])
    data["y_test"] = torch.tensor(data["y_test"], dtype=torch.long)
    return data

def tensor_to_torch_dataset_converter(data):
    dict = {}
    dict["train"] = data_set(data["x_train"],data["y_train"])
    dict["test"] = data_set(data["x_test"], data["y_test"])
    return dict






