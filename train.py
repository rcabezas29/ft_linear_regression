import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
	data = pd.read_csv("./data.csv")
	km = list(data.km)
	price = list(data.price)

	plt.scatter(km, price)
	plt.xlabel("KM")
	plt.ylabel("Price")
	plt.show()
	# df = pd.DataFrame(data)

	# df.plot.scatter(x="km", y="price")
