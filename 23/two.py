class Elve:

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.proposal = None

    def getPosition(self) -> "tuple[int, int]":
        return (self.x, self.y)

    def setPosition(self, position: "tuple[int,int]") -> None:
        self.x = position[0]
        self.y = position[1]

    def stayPut(self):
        self.proposal = None

    def propose(self, proposal: "tuple[int, int]"):
        self.proposal = proposal

elves: "list[Elve]" = []
elveMap: "dict[tuple[int,int], Elve]" = {}

readingY = 0

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        readingX = 0
        for c in line:
            if c == "#":
                elve = Elve(readingX, readingY)
                elves.append(elve)
                elveMap[elve.getPosition()] = elve
            readingX += 1
        readingY += 1

class Direction:

    def __init__(self, name: str, x: int, y: int, checks: "list[tuple[int, int]]") -> None:
        self.name = name
        self.x = x
        self.y = y
        self.checks = checks

directions: "list[Direction]" = [
    Direction('north', 0, -1, [(-1,-1), ( 0,-1), ( 1,-1)]),
    Direction('south', 0,  1, [(-1, 1), ( 0, 1), ( 1, 1)]),
    Direction('west', -1,  0, [(-1,-1), (-1, 0), (-1, 1)]),
    Direction('east',  1,  0, [( 1,-1), ( 1, 0), ( 1, 1)])
]

def countNeighbours(cx, cy):
    count = 0
    for x in range(cx-1, cx+2):
        for y in range(cy-1, cy+2):
            if (x != cx or y != cy) and elveMap.get((x, y)) != None:
                count += 1
    return count

def countElves(cx, cy, checks):
    count = 0
    for check in checks:
        x = cx + check[0]
        y = cy + check[1]
        if elveMap.get((x, y)) != None:
            count += 1
    return count

def step():
    anyProposal = False
    proposalCounter: "dict[tuple[int, int], int]" = {}
    for elve in elves:
        elve.stayPut()
        if countNeighbours(elve.x, elve.y) > 0:
            for direction in directions:
                if countElves(elve.x, elve.y, direction.checks) == 0:
                    proposal = (elve.x + direction.x, elve.y + direction.y)
                    elve.propose(proposal)
                    anyProposal = True
                    if proposalCounter.get(proposal) == None:
                        proposalCounter[proposal] = 1
                    else:
                        proposalCounter[proposal] = proposalCounter[proposal] + 1
                    break
    
    for elve in elves:
        if elve.proposal != None and proposalCounter[elve.proposal] == 1:
            elveMap.pop(elve.getPosition())
            elveMap[elve.proposal] = elve
            elve.setPosition(elve.proposal)

    directions.append(directions.pop(0))
    return anyProposal


def printMap():
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0
    for elve in elves:
        minX = min(minX, elve.x)
        maxX = max(maxX, elve.x)
        minY = min(minY, elve.y)
        maxY = max(maxY, elve.y)

    print(minX, minY, maxX, maxY)
    count = 0    
    for y in range(minY, maxY+1):
        line = ""
        for x in range(minX, maxX+1):
            if elveMap.get((x, y)) == None:
                line = line + "."
                count += 1
            else:
                line = line + "#"
        print(line)
    print(count)
    print()

printMap()

counter = 1
while step():
    counter += 1

printMap()
print(counter)
