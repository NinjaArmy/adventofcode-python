# Day 2 - Advent of Code Python
import re

file = open('input.txt', 'r')
myList = file.readlines()

validCount = 0

for i in myList:
    # Getting min and max values containing 1 number
    if i[1] == '-':
        lowMin = int(i[0])
        if i[3] == ' ':
            lowMax = int(i[2])
            check = i[4]       
            checkString = i
            count = len(re.findall(check, checkString))
            if count - 1 >= lowMin and count - 1 <= lowMax:
                validCount += 1
        else:
            max1 = i[2]
            max2 = i[3]

            letterMax = max1 + max2
            endmax = int(letterMax)
            
            check = i[5]
            
            # I should do this in a function..
            checkString = i
            count = len(re.findall(check, checkString))

            if count - 1 >= lowMin and count - 1 <= endmax:
                validCount += 1


    # Getting min values containing 2 numbers
    if i[1] != '-':
        min1 = i[0]
        min2 = i[1]

        # Putting String together
        letterMin = min1 + min2
        endmin = int(letterMin)
        

        # MinVale is already containing 2 numbers --> max also has two numbers
        max1 = i[3]
        max2 = i[4]

        letterMax = max1 + max2
        endmax = int(letterMax)
        
        check = i[6]

        checkString = i
        count = len(re.findall(check, checkString))

        if(count - 1 >= endmin and count - 1 <= endmax):
            validCount += 1


print(validCount)
print(len(myList))
