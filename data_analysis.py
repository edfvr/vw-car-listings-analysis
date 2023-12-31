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
    print(f"The most expensive VW listed is a Volkswagen {most_expensive_car.model}, {most_expensive_car.year}")
    print(f"Details: {most_expensive_car}\n")

#------------------Average price for Golfs------------------------
    golf_models = []

    for car in cars:
        if car.model == 'Golf':
            golf_models.append(car)

    golf_prices = [int(car.price) for car in golf_models]
    
    average_golf_price = sum(golf_prices) / len(golf_prices)

    print(f"The average price for VW Golfs is {average_golf_price:.2f}\n")

#------------------Average mileage for 2020 Polos------------------------
    y2020_polo_models = []

    for car in cars:
        if car.model == 'Polo' and car.year == '2020':
            y2020_polo_models.append(car)

    polo_mileages = [int(car.mileage) for car in y2020_polo_models]

    average_polo_mileage = sum(polo_mileages) / len(polo_mileages)

    print(f"The average mileage for Polos is {average_polo_mileage:.2f}")