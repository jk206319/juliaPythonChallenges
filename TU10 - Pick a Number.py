# Exercise 1: Make a number generator for floats between 0.1 and 9.9
import random
numberGeneratorOne = random.uniform(0.1, 99)
print(numberGeneratorOne)

# EXERCISE 2: Put it all together.
# Make a program that picks a name at random and then gives the user the choice to keep it in the list or not.
chooseCast = ['Wednesday', 'Enid', 'Tyler', 'Xavier', 'Ms. Thornhill']
for i in range(1,4):
    chosenCast = random.choice(chooseCast)
    print(chosenCast)
# Write your code here :-)
