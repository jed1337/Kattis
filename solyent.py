from math import ceil
test_cases = int(input())

for i in range(test_cases):
    calorie_requirement = int(input())
    bottles_needed = calorie_requirement/400
    print(ceil(bottles_needed))