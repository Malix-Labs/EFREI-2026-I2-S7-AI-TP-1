import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn import datasets
import matplotlib.pyplot as plt

#------------ Parameters -----------#
'''Define your hyper-parameters in this place'''

# --------- Functions  ---------------#
class LinearRegression:

    def __init__(self):
        ''' Initialization of Linear Regression "hyper-parameters"  '''

    def sigmoid(self,z):
        '''sigmoid activation function : returns a real number'''

    def train_GDA(self,X, y):
        '''
        - Training function    : GDA - Gradient Descent Algorithm
        - Stopping criteration : Maxiterations
        - Each feature needs to correspond to a weight
        '''
 
        print("Weights = ",self.weights," and Bias = ",self.bias)

    def accuracy(self,y_true, y_pred):
        '''Accuracy function : y' vs y : returns % accuracy '''

    def predict(self,X):
        '''
        - The prdiction function : returns y_predicted
        - Applying a threshold of 0.5
        '''

    def plot_results(self, y_target, y_pred, accuracy, name):
        '''
        -plot a barplot for y_target
        -plot a barplot for y_pred
        -show accuracy of the model in title
        -save results in "pdf" format
        '''

# --------- Testing ---------------#
if __name__ == "__main__":

    '''
    -You need to call all your function in here.
    -To code your model, you only need "numpy" !
    -Scklearn is only used to import dataSets  !

    1) Import your data set (from scklearn) with "make_regression" function
    2) Pre_process them if needed
    3) Train your model
    4) Teste your model and display the mean squared error
    5) Plot results
    - Repeat the five steps on different parameters of your dataset, on different hyper-parameters. 
    - Compare Results
    '''