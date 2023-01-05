# Write your code here :-)
# Exercise 1: Create a list of number and total it up.

numberList = [45678, 35832, 728]
sum(numberList)
print(sum(numberList))

# EXERCISE 2: Create a list's vital statistics including total, minimum, maxiumum, length & mean average
longList = [1, 2, 4, 3, 9, 4, 16, 5, 25, 6, 36, 7, 49, 8, 64]
print('Maximum:')
print(max(longList))

print('Minimum:')
print(min(longList))

print('Length')
print(len(longList))

print('Mean average')
add = int((sum(longList)))
length = int((len(longList)))

average = add / length

print(round(average,1))

