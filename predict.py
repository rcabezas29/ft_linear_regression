def catch_tethas():
    try:
        with open('.theta') as file:
            t1, t2 = file.read().split(',')
            return float(t1), float(t2)
    except:
        return 0.0, 0.0

def	estimate_price(mileage):
	theta0, theta1 = catch_tethas()
	return theta0 + (theta1 * mileage)

if __name__ == '__main__':
    try:
        mil = float(input('Input a mileage: '))
    except:
        print('Wrong input')
    else:
        print(f'The expected cost for that mileage is {estimate_price(mil)}')