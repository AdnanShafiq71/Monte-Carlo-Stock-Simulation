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
for i in range(1000):
    step = random.uniform(-10, 10)
    price = price + step

#We cannot have a price below 0 in the market for this asset. I want to ensure that the price never goes below 0 using an if statement
    if price <= 0:
        price = 0
        history.append(price)
print(history)

#I have installed the library called matplotlib to create a visual representation of the price changes
import matplotlib.pyplot as plt
plt.plot(history)
plt.title("Simple Random Walk")
plt.xlabel("Days")
plt.ylabel("Price")
plt.show()