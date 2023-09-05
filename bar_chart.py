import pandas as pd
import matplotlib.pyplot as plt

cars = pd.read_csv('vw.csv')

model_avg_mileage = cars.groupby('model')['mileage'].mean().reset_index()

plt.bar(
    model_avg_mileage.model,
    model_avg_mileage.mileage
    )
plt.xlabel("Model")
plt.ylabel("Average Mileage")
plt.title("Average mileages of VW models")
plt.show()