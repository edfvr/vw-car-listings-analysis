import csv
from collections import namedtuple

Car = namedtuple("Car", "model year price transmission mileage fuelType tax mpg engineSize")

with open("vw.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)

    cars = [Car(*row) for row in reader]

    most_expensive_car = cars[0]
    for car in cars:
        if int(car.price) > int(most_expensive_car.price):
            most_expensive_car = car
    print(most_expensive_car)