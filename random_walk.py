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
#I want to tell python to make the price take 100 steps

print("Loop is starting...") # Diagnostic print

for i in range(390):
    step = random.uniform(-10, 10)
    price = price + step
    times.append(times[-1] + timedelta(minutes=1)) #Increases the time by one minute for each step
    
    if price <= 0:
        price = 0
        history.append(price)
        print("Stock went bankrupt!")
        break
    
    history.append(price)

print(f"Loop finished. Items in history: {len(history)}")
print(history)

#I have installed the library called matplotlib to create a visual representation of the price changes
import matplotlib.pyplot as plt
plt.plot(history)
plt.title("Simple Random Walk")
plt.xlabel("Time (minutes)")
plt.ylabel("Price")
plt.show()