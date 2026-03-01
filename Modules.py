# Q11. Create Custom Module
# Question: Create operations.py with square() and cube() functions and import it.
# Step 1: Create file → operations.py

def square(n):
    return n * n

def cube(n):
    return n * n * n
  
# Step 2: Main Program (another file)

import operations
num = int(input("Enter a number: "))
print("Square:", operations.square(num))
print("Cube:", operations.cube(num))


# Q12. Random Guess Game
# Question: Generate random number (1–100) and build guessing game using loop.

import random
secret = random.randint(1, 100)
while True:
    guess = int(input("Guess the number (1-100): "))
    
    if guess > secret:
        print("Too High!")
    elif guess < secret:
        print("Too Low!")
    else:
        print("Correct! You guessed it ")
        break


# Q13. Math Module Usage
# Question: Use math module to calculate square root, power, and factorial.

import math
num = int(input("Enter a number: "))
print("Square Root:", math.sqrt(num))
print("Power (num^2):", math.pow(num, 2))
print("Factorial:", math.factorial(num))
