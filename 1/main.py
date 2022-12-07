import bisect
from functools import reduce

with open('./input.txt', 'r') as input:
    topCalories = [];
    currentCalories = 0; 
    for line in input:
        if len(line) == 1:
            bisect.insort(topCalories, currentCalories)
            while len(topCalories) > 3:
                    topCalories.pop(0)
            currentCalories = 0
        else:
            currentCalories += int(line)
    print(topCalories)
    sum = reduce(lambda a, b: a+b, topCalories)
    print(sum)
