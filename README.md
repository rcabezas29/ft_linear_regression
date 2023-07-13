# ft_linear_regression

## Description

This project is an introduction to the basic concept behind machine learning.  
This project consists of the creation of a program that predicts the price of a car  
by using a linear function train with a [gradient descent](https://en.wikipedia.org/wiki/Gradient_descent) algorithm.

## Programs

### train.py
This is the training program. It iterates the dataset thousands of times  
in order to ajust *theta0* and *theta1* (the constant and the slope of a linear function) to the data.  

![](https://latex.codecogs.com/svg.image?tmp&space;\theta_{0}&space;=&space;\alpha&space;*&space;\frac{1}{m}&space;\sum_{i&space;=&space;0}^{m&space;-&space;1}(estimatePrice(mileage[i])&space;-&space;price[i]))
![](https://latex.codecogs.com/svg.image?tmp&space;\theta_{1}&space;=&space;\alpha&space;*&space;\frac{1}{m}&space;\sum_{i&space;=&space;0}^{m&space;-&space;1}(estimatePrice(mileage[i])&space;-&space;price[i])&space;*&space;mileage[i])

![](./Train.mov)

After the whole training, it stores *theta0* and *theta1* into `.theta`.

### predict.py
The program will ask the user for an input (mileage) to predict how much would be the cost of that mileage.  
It takes *theta0* and *theta1* from `.theta` to do the prediction. It uses 0.0 as default values.

![](https://latex.codecogs.com/svg.image?estimatePrice(mileage)&space;=&space;\theta&space;_{0}&space;&plus;&space;(\theta_{1}&space;*&space;mileage))

### prediction_accuracy.py
This program measures the accuracy of the prediction based on the prediction of the values it already knows.

## Usage

```
pip3 install -r requirements.txt
```
TRY
```
python3 train.py
```
```
python3 predict.py
```
```
python3 prediction_accuracy.py
```

## References
[Stanford Supervised Machine Learning Course on Coursera - Andrew Ng ](https://www.coursera.org/learn/machine-learning)