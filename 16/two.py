import re
import bisect

expression = 'Valve ([A-Z]{2}) has flow rate=([0-9]+); tunnels? leads? to valves? ([A-Z]{2}(, [A-Z]{2})*)'

rooms = dict()
nonZeroRooms = []
potential = 0

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        match = re.match(expression, line)
        label = match.group(1)
        pressure = int(match.group(2))
        rooms[label] = {'pressure': pressure, 'connections': match.group(3).split(', ')}
        
        if pressure > 0:
            potential += pressure
            nonZeroRooms.append(label)

class Path:

    def __init__(self):
        self.lastRoom = ['AA', 'AA']
        self.openValves = []
        self.timeLeft = [26, 26]
        self.pressure = 0
        self.potential = potential
        self.calcWeight()

    def copy(self):
        other = Path()
        other.lastRoom = self.lastRoom.copy()
        other.openValves = self.openValves.copy()
        other.timeLeft = self.timeLeft.copy()
        other.pressure = self.pressure
        other.potential = self.potential
        return other

    def addRoom(self, id, roomSequence):
        self.timeLeft[id] -= (len(roomSequence) + 1)
        lastRoom = roomSequence[-1]
        self.lastRoom[id] = lastRoom

        pressureRelease = rooms[lastRoom]['pressure']
        self.pressure += pressureRelease * self.timeLeft[id]
        self.openValves.append(lastRoom)
        self.potential -= pressureRelease
        self.calcWeight()

    def shorterId(self):
        if self.timeLeft[0] > self.timeLeft[1]:
            return 0
        else:
            return 1

    def calcWeight(self):
        #potential = 0
        #for room in nonZeroRooms:
        #    if not room in self.openValves:
        #        len0 = len(pathToRoom(self.lastRoom[0], room))
        #        len1 = len(pathToRoom(self.lastRoom[1], room))
        #        time = max(self.timeLeft[0] - len0, self.timeLeft[1] - len1)
        #        if time > 0:
        #            potential += time * rooms[room]['pressure']
        #        
        #self.weight = - potential - self.pressure
        self.weight = - self.pressure


    def print(self):
        print(self.pressure, self.potential, self.openValves)

pathCache = dict()

def pathToRoom(start, end):
    cacheKey = start+end
    if cacheKey in pathCache:
        return pathCache[cacheKey]

    candidates = [[start]]
    while len(candidates) > 0:
        candidate = candidates.pop(0)
        for next in rooms[candidate[-1]]['connections']:
            if next == end:
                candidate.append(next)
                pathCache[cacheKey] = candidate
                return candidate
            
            if candidate.count(next) == 0:
                new = candidate.copy()
                new.append(next)
                candidates.append(new)

for label in nonZeroRooms:
    for otherLabel in nonZeroRooms:
        if label != otherLabel:
            pathToRoom(label, otherLabel)

paths = [Path()]
sampler = 0

bestSolution = Path()
while len(paths) > 0:
    currentPath = paths.pop(0)
    if(currentPath.pressure > bestSolution.pressure):
        bestSolution = currentPath
        print('new sol', bestSolution.pressure)

    shorterId = currentPath.shorterId()

    sampler = sampler + 1
    if sampler % 100000 == 0:
        currentPath.print()
        print(sampler, len(paths), currentPath.timeLeft, currentPath.weight, paths[-1].weight)
        print('current best solution', bestSolution.pressure)
        print()

    currentRoom = currentPath.lastRoom[shorterId]
    
    for nextTarget in nonZeroRooms:
        if currentPath.openValves.count(nextTarget) == 0:
            pathToTarget = pathToRoom(currentRoom, nextTarget)[1:]
            if len(pathToTarget) <= currentPath.timeLeft[shorterId] + 2:
                nextPath = currentPath.copy()    
                nextPath.addRoom(shorterId, pathToTarget)
                bisect.insort(paths, nextPath, key= lambda path: path.weight)