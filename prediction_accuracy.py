import pandas as pd
from predict import estimate_price, catch_tethas
from numpy import mean

if __name__ == '__main__':
	data = pd.read_csv("./data.csv")
	diff = []
	for	_, row in data.iterrows():
		prediction = estimate_price(row.km)
		difference = abs((row.price - prediction) / row.price * 100)
		diff.append(difference)

	accuracy = 100 - mean(diff)

	print(f'The precision has a precision of {accuracy}%')