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


# Part - 2
for i in numbersArray:
    for j in numbersArray:
        for k in numbersArray:
            if i + j + k == 2020:
                partTwo = i * j * k
print(result)
print(partTwo)

