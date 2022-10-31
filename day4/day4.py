# Day 4 - Advent of Code

file = open('input.txt', 'r')


arr = file.read().split("\n\n")

counter = 0
for item in arr:
  if "byr" in item and "iyr" in item and "eyr" in item and "hgt" in item and "hcl" in item and "ecl" in item and "pid" in item:
    counter += 1

print(counter)

