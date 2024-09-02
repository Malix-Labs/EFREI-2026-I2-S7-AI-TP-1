#### TP1 : Linear and Logistic Regression

#### ST2AIM - "AI & Machine Learning" - 2024/2025

#### Author : Youssef Ait El Mahjoub

<br/>

--------------------------------------------------------------------
## <font color="red"> Objectives of the Practical Activity : </font>
--------------------------------------------------------------------

- Retrieve data
- Split and standardize data
- Implement Linear and and Logistic Regression
- Understand the behavior of both methods
- Establish the relationship between the learning rate and the convergence of the algorithms
- Establish the relationship between convergence and the loss function
<br/>

-------------------------------------------------
## <font color="red"> Reminder questions : </font>
-------------------------------------------------

1. What is the difference between Linear and Logistic regression ?
2. What about loss function ? Discuss error function shape of each method.
3. The core algorithm behind these two methods is it the same ?
4. What does "convergency" mean in both cases ?

-----------------------------------------------------------------
## <font color="red">  Part I : Linear Regression model </font>
-----------------------------------------------------------------

- You need to complete the "LnR_students.py" file.
- Tensorflow and PyTorch are not allowed !

1.  Analyze the structure of the code to understand what is expected.
<br/>

2.  Data Preparation:
    - Go to the "main" function, and retrieve the dataset "make_regression" from sklearn.
    - Standardize data if needed (i.e. centered around the mean...)
    - Split the data set, to a training set and a testing set
<br/>
<br/>

3. Implementation of Linear Regression with Gradient Descent Algorithm (GDA):
    - Complete the constructor of the "LinearRegression" class
    - Complete the function "mse()"
    - Complete the function "train_GDA(self, X, y)" which implements the Gradient Descent algorithm seen in class
    - The stopping condition should be a maximum number of iterations
    - Initialization of weights should be done randomly
    - Complete the function "predict()"
<br/>
<br/>

4. Testing the model, GDA:
    - Complete the function "predict()"
    - Apply this function to the test dataset, in the main function
    - Display the weights and bias obtained
    - Test your model with different initial weight, what do you observe ?
    - Test your model with different nFeatures and nSamples
<br/>
<br/>

5. Create a function "plot_results(self, X , y , y_pred_line, name): 
    - Display data set, as well as the regression line
    - save results in "pdf" format
<br/>
<br/>

6. Create a function "plot_loss_surface(self, X, y)" that plots a 3D landscape for a model with 2 weights:
    - X axis will coresspond to weight 1
    - Y axis will coresspond to weight 2
    - Z axis will correspond to loss funcion of the couple (weight1, weight2)
    - Display the whole surface landscape
    - Add the trajectory of weights, from the gradient descent algorithm implemented above
    - You can fix an initial weight to have representable trajectory
    - save results in "pdf" format
<br/>

----------------------------------------------------------------
## <font color="red">  Part II : Logistic Regression model </font>
-----------------------------------------------------------------

You need to complete the "LgR_students.py" file.

1.  Analyze the structure of the code to understand what is expected.
2.  Data Preparation:
    - Go to the "main" function, and retrieve the dataset "load_breast_cancer" from sklearn.
    - Standardize data if needed (i.e. centered around the mean...)
    - Split the data set, to a training set and a testing set
<br/>

3. Implementation of Logistic Regression with Gradient Descent Algorithm (GDA):
    - Complete the constructor of the "LogisticRegression" class
    - Complete the function "sigmoid()"
    - Complete the function "train_GDA(self, X, y)" which implements the Gradient Descent algorithm seen in class.
    - The stopping condition should be a maximum number of iterations.
    - Initialization of weights should be done randomly
    - Complete the function "accuracy()"
<br/>
<br/>

4. Testing the model, GDA:
    - Complete the function "predict()"
    - Apply this function to the test dataset, in the main function
    - Display the weights and bias obtained
    - Test your model with different initial weight, what do you observe ?
    - Test your model with different "nFeatures" and "nSamples"
    - Analyse "accuracy" of each experiment with "maxiterations", and "learning rate". what do you observe ?
<br/>
<br/>

5. Create a function "plot_results(self, y_target, y_pred, accuracy, name)" :
    - plot a barplot for y_target
    - plot a barplot for y_pred
    - bareplots needs to be drawn horizentaly symetrical. 
    - show accuracy of the model in title
    - save results in "pdf" format
<br/>
<br/>

4. Code Cleanup:
    - The user of your code should be able to specify the number of samples, the number of features, the learning rate, and the maximum number of iterations. Without diving into your code, but only in the header of your code.
    - Save your results in separate folders, one folder for each regression method.





