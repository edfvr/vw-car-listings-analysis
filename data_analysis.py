import csv
from collections import namedtuple

Car = namedtuple("Car", "model year price transmission mileage fuelType tax mpg engineSize")

with open("vw.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)

    cars = [Car(*row) for row in reader]

#-----------------------Most expensive car----------------------
    most_expensive_car = cars[0]
    for car in cars:
        if int(car.price) > int(most_expensive_car.price):
            most_expensive_car = car
    #print(most_expensive_car)

#------------------Average price for Golfs------------------------
    golf_models = []

    for car in cars:
        if car.model == 'Golf':
            golf_models.append(car)
    print(f"Number of Golfs = {len(golf_models)}")

    golf_prices = [float(car.price) for car in golf_models]
    print(f"Sum of Golf Prices = {sum(golf_prices)}")

    average_golf_price = sum(golf_prices) / len(golf_prices)

    print(f"The average price for VW Golfs is {round(average_golf_price, 2)}")

#------------------Average mileage for Polos------------------------
    y2020_polo_models = []

    for car in cars:
        if car.model == 'Polo' and car.year == '2020':
            y2020_polo_models.append(car)
    print(f"Number of 2020 Polo models = {len(y2020_polo_models)}")