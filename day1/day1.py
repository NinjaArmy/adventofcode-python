# Day1 Advent of Code Python

file = open('input.txt', 'r')
myList = file.readlines()



# Writing everything into an array
input = []
for line in myList:
    input = input + line.split()



# Convert String Array to int array
numbersArray = [int(i) for i in input]

for i in numbersArray:
    for j in numbersArray:
        if i + j == 2020:
            result = i * j


print(result)

