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

    def mse(self,y_true, y_pred):
        ''' Mean Squared Error : returns a scalar value '''

    def train_GDA(self,X, y):
        '''
        - Training function    : GDA - Gradient Descent Algorithm
        - Stopping criteration : Maxiterations
        - Each feature needs to correspond to a weight
        '''
 
        print("Weights = ",self.weights," and Bias = ",self.bias)

    def predict(self,X):
        ''' The prediction function : returns y_predicted '''

    def plot_results(self, X , y , y_pred_line, name):
        '''
        -plot data as scatter points
        -plots linear regression model
        -function only suppots 1 feature ! 
        -save results in "pdf" format
        '''
    
    def plot_loss_surface(self, X, y):
        ''' 
        -Function plots the 3D space of the loss function : weigth1 axis, weight2 axis and loss axis
        -Plots the optimal trajectory, from random initial weights, to optimal weights
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
    5) Plot the regression line
    - Repeat the five steps on different parameters of your dataset, on different hyper-parameters. 
    - Compare Results
    6) Plot optimal trajctory of GDA algorithm in loss landscape space
    '''