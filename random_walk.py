#I am importing the random module to generate random numbers
import random

#I am generating a random number between -10 and 10 and storing it as the variable 'step'
#I could choose random.randint if I wanted to generate a random integer however, a random decimal seems more appropriate for a fluctuating stock price
step = random.uniform(-10, 10)
#I am printing the value of 'step' to the console
print(step)
