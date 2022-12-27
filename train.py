import pandas as pd
import matplotlib.pyplot as plt
from predict import estimate_price, catch_tethas
import numpy as np

def	show_graphic(data, theta0, theta1):
	km = list(data.km)
	price = list(data.price)

	plt.scatter(km, price)
	x = np.linspace(22899, 240000, 100)
	y = theta1 * x + theta0
	plt.plot(x, y, '-r', label='y = mx + k')
	plt.xlabel("KM")
	plt.ylabel("Price")
	plt.show()

def	normalize(data):
	normalized_df = (data-data.min()) / (data.max() - data.min())
	return(normalized_df)

def	cost_function(kms, prices):
	m = kms.size
	x =  0.1 * (1 / m) * sum(estimate_price(kms) - prices)
	y = 0.1 * (1 / m) * sum((estimate_price(kms) - prices) * kms)

	return x, y


def	linear_regression(data):
	data = normalize(data)
	X = data.iloc[:, 0]
	Y = data.iloc[:, 1]

	theta0, theta1 = catch_tethas()

	for _ in range(1000):
		tmp_theta0, tmp_theta1 = cost_function(X, Y)
		theta0 -= tmp_theta0
		theta1 -= tmp_theta1

		# error = cost_function(kms, prices)

		with open('.theta', 'w') as f:
			f.write(f'{theta0},{theta1}')
			f.close()
	return theta0, theta1

if __name__ == '__main__':
	data = pd.read_csv("./data.csv")

	theta0, theta1 = linear_regression(data)
	show_graphic(data, theta0, theta1)

