from RBF_net import *
import extraFuncs as funcs
import numpy as np
from matplotlib import pyplot as plt
""" Initialize random generator """
np.random.seed()

def learn_regression():
    """
        Loading training and test data
    """
    train = funcs.training_data_from_file("training_data",float,True)
    test = funcs.training_data_from_file("test_data",float,True)

    """
        Initializing parameters for RBF net
    """
    k = int(input("#RBF neurons: "))
    random_centers = tmp = np.random.rand(k) * 40
    print("centers: ",random_centers)
    dim = [1,k,1]
    learnrate = float(input("Learnrate: "))

    RBF_regr = RBF(dim,random_centers,learnrate)

    """
        Learn-loop: computes the error and saves it. Also does a live plot of the regression
    """
    interactive = int(input("Interactive draw mode? "))
    Loss = []
    iterations = int(input("#learning iterations: "))
    for i in range(iterations):
        RBF_regr.learn_weights(train)
        Loss.append(RBF_regr.learn_weights(test,learn=False))
        """
            Prepare plot data
        """
        X = np.arange(0,40,0.01)
        RBF_regr.compute_distance(np.reshape(X, (len(X), 1)))
        predictions = RBF_regr.get_predictions()
        teacher = [funcs.teacher_func(x) for x in X]
        """
            Plot data
        """
        if interactive:
            if i%(iterations/10) == 0:
                title = "RBF net regression: " + str(dim) + "\niteration: " + str(i)
                xlabel = "x-axis"
                ylabel = "f(x)"
                funcs.plot(X=X,
                           Y=teacher,
                           title=title,
                           xlabel=xlabel,
                           ylabel=ylabel,
                           filename=None,
                           close=False,
                           save=False,
                           label="f(x)=0.02 * x * x * x - 1.06 * x * x + 15 * x")
                funcs.plot( X=X,
                            Y=predictions,
                            title=title,
                            xlabel=xlabel,
                            ylabel=ylabel,
                            filename=None,
                            close=False,
                            save=False,
                            label="RBF prediction")
                plt.pause(0.05)
                plt.clf()

    """
        Actual plotting happens here. The plotting might happen in plt.pause(0.05) because
        it seems to show the plot for some reason. The code below just makes sure that the interactive learned
        prediction is plotted anyway
    """
    if interactive:
        plt.show()
        plt.close()
    """
        Generating png for comparison of the function and the prediction of the RBF net
        and png for the learning curve
    """
    X = np.arange(0,40,0.01)
    RBF_regr.compute_distance(np.reshape(X,(len(X),1)))
    predictions = RBF_regr.get_predictions()
    predictions = np.reshape(predictions,predictions.shape[0])
    teacher = [funcs.teacher_func(x) for x in X]

    """
        png:Learning curve
    """
    title = "RBF: regression learning curve with \n" + str(dim)
    xlabel = "iterations"
    ylabel = "E(Patterns)"
    filenname = "RBF_regression_learningcurve"
    funcs.plot(range(1,len(Loss)+1), Loss, title, xlabel, ylabel, filenname,label="p")

    """
        png:Comparison
    """
    title = "Regression: comparison: predictions with teacher"+str(dim)
    xlabel = "x-axis"
    ylabel = "f(x)"
    filenname = "Regression_comparison"
    funcs.plot( X=X,
                Y=teacher,
                title=title,
                xlabel=xlabel,
                ylabel=ylabel,
                filename=filenname,
                close=False,
                save=False,
                label="f(x)=0.02 * x * x * x - 1.06 * x * x + 15 * x")
    funcs.plot( X=X,
                Y=predictions,
                title=title,
                xlabel=xlabel,
                ylabel=ylabel,
                filename=filenname,
                close=True,
                save=True,
                label="RBF prediction")

learn_regression()