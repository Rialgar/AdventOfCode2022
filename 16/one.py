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
            potential += int(match.group(2))
            nonZeroRooms.append(label)

class VisitedRoom:

    def __init__(self, label: str, openValve: bool):
        self.label = label
        self.pressure = rooms[label]['pressure']
        self.openValve = openValve

class Path:

    def __init__(self):
        self.rooms = [VisitedRoom('AA', False)]
        self.openValves = []
        self.timeLeft = 30
        self.pressure = 0
        self.potential = potential

    def copy(self):
        other = Path()
        other.rooms = self.rooms.copy()
        other.openValves = self.openValves.copy()
        other.timeLeft = self.timeLeft
        other.pressure = self.pressure
        other.potential = self.potential
        return other

    def addRoom(self, room: VisitedRoom):
        self.rooms.append(room)
        self.timeLeft -= 1
        if room.openValve:
            self.timeLeft -= 1
            self.pressure += room.pressure * self.timeLeft
            self.openValves.append(room.label)
            self.potential -= room.pressure

    def weight(self):
        return -self.potential * (self.timeLeft*3/4) - self.pressure

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
            
            new = candidate.copy()
            new.append(next)
            candidates.append(new)

paths = [Path()]

while paths[0].timeLeft > 0 and paths[0].potential > 0:
    currentPath = paths.pop(0)
    print(len(paths), currentPath.timeLeft, currentPath.weight())

    currentRoom = currentPath.rooms[-1].label
    for nextTarget in nonZeroRooms:
        if currentPath.openValves.count(nextTarget) == 0:
            pathToTarget = pathToRoom(currentRoom, nextTarget)[1:-1]
            if len(pathToTarget) < currentPath.timeLeft + 2:
                nextPath = currentPath.copy()
                for nextRoomLabel in pathToTarget:
                    nextPath.addRoom(VisitedRoom(nextRoomLabel, False))        
                nextPath.addRoom(VisitedRoom(nextTarget, True))
                bisect.insort(paths, nextPath, key= lambda path: path.weight())

for room in paths[0].rooms:
    print(room.label, room.openValve)

print(paths[0].pressure)