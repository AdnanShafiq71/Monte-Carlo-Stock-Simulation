
#Current formula: Price(t+1) = Price(t) * (1 + percentage change)

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.dates as mdates

#I want the x axis of the graph to have time rather than counting the number of steps as days. I want to make each step one minute
from datetime import datetime, timedelta
start_time = datetime(2026, 4, 1, 9, 30) #Starting time of the stock market
times = [start_time]

#I am importing the random module to generate random numbers
import random

#I want to run this random walk multiple times as a Monte Carlo simulation
simulations = 1000

#I am adding volatility to the price changes. Some days may be quiet and some more volatile. We need a variable that can represent this.
volatility = 0.01

#I am generating a random number between -10 and 10 and storing it as the variable 'step'
#I could choose random.randint if I wanted to generate a random integer however, a random decimal seems more appropriate for a fluctuating stock price
step = random.uniform(-volatility, volatility)

#I am printing the value of 'step' to the console
print(step)

#I want to create a starting point for the price
price = 1000

#I want to show the history of the price changes after every step
history = [price]

#I want to add drift to the price changes. Drift is a constant value that represents the expected return of the stock over time.
drift = 0.0001

plt.figure(figsize=(12, 7))

#I want to run the random walk 1000 times to see the different possible outcomes of the stock price.
for s in range(simulations):
    price = 1000
    history = [price]

    #I want to tell python to make the price take 390 steps
    for i in range(390):
        change_percentage = random.uniform(-volatility, volatility)
        price = price * (1 + change_percentage + drift)
    
        if price <= 0:
            price = 0
            history.append(price)
            break
        history.append(price)

    plot_times = [start_time + timedelta(minutes=j) for j in range(len(history))]
    plt.plot(plot_times, history, alpha = 0.05, linewidth = 0.5, color = "blue")

plt.title("Monte Carlo Simulation of Stock Price Changes")
plt.xlabel("Time (minutes)")
plt.ylabel("Stock Price ($)")

# Getting the current "axes" (the plot itself)
ax = plt.gca()

# Formatting the time to only show Hour:Minute
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Telling the graph to only show a label every 30 minutes
ax.xaxis.set_major_locator(mdates.MinuteLocator(byminute=[0, 30]))

# Tilting the labels so they don't overlap
plt.gcf().autofmt_xdate()
plt.grid(True, linestyle=':', alpha=0.05)
plt.show()