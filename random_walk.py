
#Current formula: Price(t+1) = Price(t) + step


import matplotlib.dates as mdates

#I want the x axis of the graph to have time rather than counting the number of steps as days. I want to make each step one minute
from datetime import datetime, timedelta
start_time = datetime(2026, 4, 1, 9, 30) #Starting time of the stock market
times = [start_time]

#I am importing the random module to generate random numbers
import random

#I am generating a random number between -10 and 10 and storing it as the variable 'step'
#I could choose random.randint if I wanted to generate a random integer however, a random decimal seems more appropriate for a fluctuating stock price
step = random.uniform(-10, 10)
#I am printing the value of 'step' to the console
print(step)

#I want to create a starting point for the price
price = 1000
#I want to show the history of the price changes after every step
history = [price]

#I want to tell python to make the price take 390 steps

for i in range(390):
    step = random.uniform(-10, 10)
    price = price + step
    
    if price <= 0:
        price = 0
        history.append(price)
        break

    history.append(price)

plot_times = [start_time + timedelta(minutes=j) for j in range(len(history))]
#I have installed the library called matplotlib to create a visual representation of the price changes
import matplotlib.pyplot as plt

plot_times = [start_time + timedelta(minutes=j) for j in range(len(history))]

plt.plot(plot_times, history)
plt.title("Simple Random Walk")
plt.xlabel("Time (minutes)")
plt.ylabel("Price")
# 1. Get the current "axes" (the plot itself)
ax = plt.gca()

# 2. Format the time to only show Hour:Minute (e.g., 09:30)
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# 3. Tell the graph to only show a label every 30 minutes
ax.xaxis.set_major_locator(mdates.MinuteLocator(byminute=[0, 30]))

# 4. Tilt the labels so they don't overlap (optional but looks pro)
plt.gcf().autofmt_xdate()
plt.show()