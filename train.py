import pandas as pd
import matplotlib.pyplot as plt
from predict import estimate_price, catch_tethas
import numpy as np
from tqdm import tqdm

def	show_graphic(data):
	km = list(data.km)
	price = list(data.price)
	theta0, theta1 = catch_tethas()
	theta0, theta1 = denormalize_thetas(data, theta0, theta1)

	plt.clf()
	plt.scatter(km, price)
	x = np.linspace(data['km'].min(), data['km'].max())
	y = theta1 * x + theta0
	plt.plot(x, y, '-r', label='y = mx + k')
	plt.xlabel("KM")
	plt.ylabel("Price")
	plt.pause(0.01)
	plt.draw()

def	assign_thetas(theta0, theta1):
	with open('.theta', 'w') as f:
		f.write(f'{theta0},{theta1}')
		f.close()

def	denormalize_thetas(data, theta0, theta1):
	x = data['km']
	y = data['price']
	theta0 = theta0 * (max(y) - min(y)) + min(y) + (theta1 * min(x) * (min(y) - max(y))) / (max(x) - min(x))
	theta1 = theta1 * (max(y) - min(y)) / (max(x) - min(x))
	return theta0, theta1

def	normalize_data(data):
	normalized_df = (data - data.min()) / (data.max() - data.min())
	kms = normalized_df['km']
	prices = normalized_df['price']
	return kms, prices

def	cost_function(data):
	kms, prices = normalize_data(data)
	m = kms.size

	x =  0.1 * (1 / m) * sum(estimate_price(kms) - prices)
	y = 0.1 * (1 / m) * sum((estimate_price(kms) - prices) * kms)

	return x, y

def	linear_regression(data):
	theta0, theta1 = catch_tethas()

	for _ in tqdm(range(5000)):
		tmp_theta0, tmp_theta1 = cost_function(data)

		theta0 -= tmp_theta0
		theta1 -= tmp_theta1

		assign_thetas(theta0, theta1)
		show_graphic(data)
	
	theta0, theta1 = denormalize_thetas(data, theta0, theta1)
	assign_thetas(theta0, theta1)


if __name__ == '__main__':
	data = pd.read_csv("./data.csv")
	linear_regression(data)
