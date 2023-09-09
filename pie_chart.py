import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_csv('vw.csv')

number_of_cars_by_fuel = cars.groupby('fuelType')[['model']].count().sort_values('model', ascending=False).reset_index()

plt.pie(number_of_cars_by_fuel.model, labels=number_of_cars_by_fuel.fuelType, autopct='%1.1f%%')
plt.show()