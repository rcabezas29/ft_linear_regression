def catch_tethas():
    try:
        with open('.theta') as file:
            t1, t2 = file.read().split(',')
            return float(t1), float(t2)
    except:
        print('.theta file does not exists or it has an error. Thetas set to 0')
        return 0.0, 0.0

if __name__ == '__main__':
    theta0, theta1 = catch_tethas()
    try:
        mil = float(input('Input a mileage: '))
    except:
        print('Wrong input')
    else:
        print(f'The expected cost for that mileage is {theta0 + (theta1 * mil)}')