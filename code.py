import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math
import codecademylib3
 
 
## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())
 
## Analyze Coach Prices for 8-Hour Flights
print(np.mean(flight.coach_price))
print(np.median(flight.coach_price))

sns.histplot(flight.coach_price)
plt.show()
plt.clf()
 
##Analyze Coach Prices for 8-Hour Flights
print(np.mean(flight.coach_price[flight.hours == 8]))
print(np.median(flight.coach_price[flight.hours == 8]))

sns.histplot(flight.coach_price[flight.hours == 8])
 
plt.show()
plt.clf()
 

## Distribution of Flight Delays (≤ 500 minutes)
sns.histplot(flight.delay[flight.delay <=500])
plt.show()
plt.clf()
 

## Relationship Between Coach and First-Class Prices
perc = 0.1
flight_sub = flight.sample(n = int(flight.shape[0]*perc))
 
sns.lmplot(x = "coach_price", y = "firstclass_price", data = flight_sub, line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()
 

## Impact of In-Flight Amenities on Coach Prices
# Inflight Meals
sns.histplot(flight, x = "coach_price", hue = flight.inflight_meal)
plt.show()
plt.clf()
 
# Inflight Entertainment
sns.histplot(flight, x = "coach_price", hue = flight.inflight_entertainment)
plt.show()
plt.clf()
 
# Inflight WiFi
sns.histplot(flight, x = "coach_price", hue = flight.inflight_wifi)
plt.show()
plt.clf()
 

## Relationship Between Flight Hours and Passenger Count

sns.lmplot(x = "hours", y = "passengers", data = flight_sub, x_jitter = 0.25, scatter_kws={"s": 5, "alpha":0.2}, fit_reg = False)
plt.show()
plt.clf()
 
 
## Coach vs. First-Class Price Distribution by Weekend
sns.lmplot(x ='coach_price', y='firstclass_price', hue = 'weekend', data = flight_sub, fit_reg= False)
plt.show()
plt.clf()
 
 
## Coach Price Trends by Day and Redeye Status
sns.boxplot(x = "day_of_week", y = "coach_price", hue = "redeye", data = flight)
plt.show()
plt.clf()
