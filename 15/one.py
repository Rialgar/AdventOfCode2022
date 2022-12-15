import re
import bisect

targetY = 2000000
#targetY = 10
beaconX = dict()

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
            
            if(bY == targetY):
                beaconX[bY] = True

            if(sY <= targetY and targetY <= sY + delta):
                r = sY + delta - targetY
                for x in range(sX-r, sX+r+1):
                    if not x in beaconX:
                        beaconX[x] = False
            elif(sY >= targetY and targetY >= sY - delta):
                r = targetY - (sY - delta)
                for x in range(sX-r, sX+r+1):
                    if not x in beaconX:
                        beaconX[x] = False
count = 0
for key in beaconX:
    if not beaconX[key]:
        count += 1

print(count)