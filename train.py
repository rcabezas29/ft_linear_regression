import pandas as pd
import matplotlib.pyplot as plt
from predict import estimate_price, catch_tethas

def	show_graphic(data):
	km = list(data.km)
	price = list(data.price)

	plt.scatter(km, price)
	plt.xlabel("KM")
	plt.ylabel("Price")
	plt.show()

def	get_function_slope(data):
	sum = 0
	m = 0
	for index, row in data.iterrows():
		km = row.km
		price = row.price
		sum += (estimate_price(km) - price) * km
		m += 1
	
	tmp_theta1 = sum / m * 0.5
	return tmp_theta1

def	get_function_constant(data) -> float:
	sum = 0
	m = 0
	for index, row in data.iterrows():
		km = row.km
		price = row.price
		sum += (estimate_price(km) - price)
		m += 1
	
	tmp_theta0 = sum / m * 0.5
	return tmp_theta0
	

def	linear_regression(data):
	k = get_function_constant(data)
	slope = get_function_slope(data)
	with open('.theta', 'w') as f:
		f.write(f'{k},{slope}')
		f.close()


if __name__ == '__main__':
	data = pd.read_csv("./data.csv")

	for x in range(1000):
		linear_regression(data)
	show_graphic(data)



