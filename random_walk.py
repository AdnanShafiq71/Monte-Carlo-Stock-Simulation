
#Current formula: Price(t+1) = Price(t) * (1 + percentage change)

import numpy as np
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
volatility = 0.05

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
drift = 0.0002

#I want to create an expected value line in the blue cloud of the Monte Carlo simulation.
all_final_prices = []
all_histories = []

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

    all_final_prices.append(price)
    all_histories.append(history)        

    plot_times = [start_time + timedelta(minutes=j) for j in range(len(history))]


# --- CALCULATE DATA ---
mean_path = np.mean(all_histories, axis=0)
final_time_axis = [start_time + timedelta(minutes=j) for j in range(391)]
final_mean_price = mean_path[-1]

# --- CREATING THE SINGLE FIGURE ---
# Calculate how many of the 1000 runs ended above the $1000 starting price
wins = sum(1 for p in all_final_prices if p > 1000)
prob_profit = (wins / simulations) * 100
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7), gridspec_kw={'width_ratios': [2, 1]})

# --- DRAWING THE CLOUD ---
for h in all_histories:
    ax1.plot(final_time_axis, h, color="blue", alpha=0.02, linewidth=0.5)

# Plotting the Mean Path on ax1
ax1.plot(final_time_axis, mean_path, color="red", linewidth=3, label="Average Path")

# ADDING THE LABEL BACK
ax1.text(final_time_axis[-1], final_mean_price, f'  Expected: ${final_mean_price:.2f}', 
         color="red", fontweight="bold", va="center")

# Visual formatting for ax1
ax1.axhline(y=1000, color="black", linestyle="--", alpha=0.5, label="Start Price")
ax1.set_title(f"Monte Carlo Simulation: {simulations} Scenarios", fontsize=12)
ax1.set_xlabel("Time of Day")
ax1.set_ylabel("Price ($)")
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
ax1.xaxis.set_major_locator(mdates.MinuteLocator(byminute=[0, 30]))
ax1.legend(loc="upper left")
ax1.grid(True, linestyle=':', alpha=0.3)

# --- DRAWING THE HISTOGRAM ---
ax2.hist(all_final_prices, bins=50, orientation='horizontal', color='blue', alpha=0.3, edgecolor='white')
ax2.axhline(y=final_mean_price, color='red', linewidth=2, linestyle='-')
ax2.set_title("Distribution of Final Prices", fontsize=12)
ax2.set_xlabel("Frequency (Count)")
# Syncing the Y-axis of the histogram with the price of the cloud
ax2.set_ylim(ax1.get_ylim()) 
ax2.text(0.5, 0.9, f"Prob. of Profit: {prob_profit:.1f}%", 
         transform=ax2.transAxes, 
         ha="center", 
         va="center", 
         fontsize=12, 
         fontweight="bold", 
         color="green",
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

# --- FINISH ---
plt.gcf().autofmt_xdate()
plt.tight_layout()
print(f"Analysis Complete. Average Final Price: ${final_mean_price:.2f}")

# --- RISK SUMMARY STATISTICS ---
max_price = max(all_final_prices)
min_price = min(all_final_prices)
avg_price = np.mean(all_final_prices)

print("-" * 30)
print(f"MONTE CARLO RISK REPORT")
print("-" * 30)
print(f"Total Simulations: {simulations}")
print(f"Probability of Profit: {prob_profit:.2f}%")
print(f"Average Final Price: ${avg_price:.2f}")
print(f"Best Case Scenario:  ${max_price:.2f}")
print(f"Worst Case Scenario: ${min_price:.2f}")
print("-" * 30)

plt.show()