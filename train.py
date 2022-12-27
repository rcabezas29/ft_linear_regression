import pandas as pd
import matplotlib.pyplot as plt
from predict import estimate_price, catch_tethas
import numpy as np

def	show_graphic(data, theta0, theta1):
	km = list(data.km)
	price = list(data.price)

	plt.scatter(km, price)
	x = np.linspace(61789, 240000, 100)
	y = theta1 * x + theta0
	plt.plot(x, y, '-r', label='y = mx + k')
	plt.xlabel("KM")
	plt.ylabel("Price")
	plt.show()

def	normalize(data, t0, t1):
	X = data['km'].tolist()
	Y = data['price'].tolist()

	norm_t0 = (t0 - min(X)) / (max(X) - min(X))
	norm_t1 = (t1 - min(Y)) / (max(Y) - min(Y))

	return norm_t0, norm_t1

def	linear_regression(data):
	t0_sum = 0
	t1_sum = 0
	m = 0

	for index, row in data.iterrows():
		km = row.km
		price = row.price

		km, price = normalize(data, km, price)

		t0_sum += (estimate_price(km) - price)
		t1_sum += (estimate_price(km) - price) * km

		m += 1
	
	tmp_theta0 = t0_sum / m * 0.1
	tmp_theta1 = t1_sum / m * 0.1

	return tmp_theta0, tmp_theta1


if __name__ == '__main__':
	data = pd.read_csv("./data.csv")

	for x in range(1000):
		theta0, theta1 = linear_regression(data)
		with open('.theta', 'w') as f:
			f.write(f'{theta0},{theta1}')
			f.close()
		show_graphic(data, theta0, theta1)

