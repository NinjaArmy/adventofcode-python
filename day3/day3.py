# Day 3 - Advent of Code

file = open('input.txt', 'r')
count = 0
index = 0
for line in file.readlines():
    if line[index % len(line.strip())] == '#':
        count += 1
    index += 3

# Task 2
# haha
file2 = open('input.txt', 'r')
countOne = 0
countTwo = 0
countThree = 0
countFour = 0
countFive = 0

indexOne = 0
indexTwo = 0
indexThree = 0
indexFour = 0
indexFive = 0
specialIndex = 0
for line in file2.readlines():
    if line[indexOne % len(line.strip())] == '#':
        countOne += 1
    if indexFive % 2 == 0:
        if line[specialIndex % len(line.strip())] == '#':
            countFive += 1
        specialIndex += 1
    if line[indexTwo % len(line.strip())] == '#':
        countTwo += 1
    if line[indexThree % len(line.strip())] == '#':
        countThree += 1
    if line[indexFour % len(line.strip())] == '#':
        countFour += 1
    indexOne += 1
    indexTwo += 3
    indexThree += 5
    indexFour += 7
    indexFive += 1


print(countOne)
print(countTwo)
print(countThree)
print(countFour)
print(countFive)

print(countOne * countTwo * countThree * countFour * countFive)
