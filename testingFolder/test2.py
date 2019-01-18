# Functions Tests
# Importing libraries
import random as ran
# To import specific stuff use following
# from random import choice


def printName(name):
    print("Hi " + name)


printName(input("Who is you? "))


# Using .format
def greet(name, name2):
    print("Hello {} and {} !".format(name, name2))


greet("Dola", "Aadil")

# Using random libary
raffle = ["Salma", "Zoya", "Alvina", "Aseel", "Nagham", "Mariam", "Serene"]
print("Raffle winner: " + ran.choice(raffle))
