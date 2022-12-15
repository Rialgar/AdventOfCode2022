import re
import time

maxCoord = 4000000
#maxCoord = 20

sensors = []

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        match = re.match('Sensor at x=(-?[0-9]+), y=(-?[0-9]+): closest beacon is at x=(-?[0-9]+), y=(-?[0-9]+)', line)
        if match != None:
            sX = int(match.group(1))
            sY = int(match.group(2))
            bX = int(match.group(3))
            bY = int(match.group(4))

            deltaX = abs(sX - bX)
            deltaY = abs(sY - bY)
            delta = deltaX + deltaY;

            sensors.append((sX, sY, delta))            

def find():
    for sensor in sensors:
        sX = sensor[0] # 5
        sY = sensor[1] # 8
        sR = sensor[2] # 3
        for x in range(sX - sR - 1, sX + sR + 2): # 1 to 9 inclusive
            if not x in range(0, maxCoord+1):
                continue

            dY = (sR - abs(x - sX) + 1)
            for y in [sY - dY, sY + dY]:
                if not y in range(0, maxCoord+1):
                    continue

                possible = True
                for sensor2 in sensors:
                    if (abs(x-sensor2[0]) + abs(y-sensor2[1])) <= sensor2[2]:
                        possible = False
                        break
                if possible:
                    print(x, y)
                    print(x * 4000000 + y)
                    return
            
find()
        