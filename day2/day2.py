# Day 2 - Advent of Code Python
import re

file = open('input.txt', 'r')
validCount = 0
validCount2 = 0

for i in file.readlines():
    # Splitting in 3dim by ' '
    (numbers, needle, phrase) = (i.split(' '))
    
    # Extracting the min and max (left and right)
    (left, right) = numbers.split('-')

    # Getting the char you need to count and strip the string
    (needle, phrase) = (needle.replace(':', ''), phrase.strip())
    
    ## Task 2
    if phrase[(int(left)) - 1] == needle and phrase[(int(right)) - 1] != needle:
            validCount2 += 1

    if phrase[(int(left)) - 1] != needle and phrase[(int(right)) - 1] == needle:
        validCount2 += 1

    # If valid input increase count by 1
    if int(left) <= phrase.count(needle) <= int(right): validCount += 1

print(validCount)
print(validCount2)
