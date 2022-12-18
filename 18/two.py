maxX = 0
maxY = 0
maxZ = 0


filledCubes = []
with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        if(len(line) > 1):
            cube = list(map(lambda n: int(n), line.split(',')))
            filledCubes.append(cube)
            maxX = max(maxX, cube[0])
            maxY = max(maxY, cube[1])
            maxZ = max(maxZ, cube[2])

# there never is a 0 in the input, by making it go to max+1 inclusive in all dimensions
# we can skip detecting checking outside the grid later

state_unknown = 0
state_outside = 1
state_lava = 2

grid = []
for x in range(maxX+2):
    grid.append([])
    for y in range(maxY+2):
        grid[x].append([])
        for z in range(maxZ+2):
            grid[x][y].append(state_unknown)

for cube in filledCubes:
    grid[cube[0]][cube[1]][cube[2]] = state_lava

# flood fill starting at known outside 0,0,0 
willBeOutside = [[0,0,0]]

def addIfNotPresent(list, entry):
    if not entry in list:
        list.append(entry)

while len(willBeOutside) > 0:
    #print(len(willBeOutside))
    next = willBeOutside.pop(0)
    grid[next[0]][next[1]][next[2]] = state_outside
    if next[0] < maxX+1 and grid[next[0]+1][next[1]][next[2]] == state_unknown:
        addIfNotPresent(willBeOutside,[next[0]+1, next[1], next[2]])
    if next[0] > 0 and grid[next[0]-1][next[1]][next[2]] == state_unknown:
        addIfNotPresent(willBeOutside,[next[0]-1, next[1], next[2]])
    if next[1] < maxY+1 and grid[next[0]][next[1]+1][next[2]] == state_unknown:
        addIfNotPresent(willBeOutside,[next[0], next[1]+1, next[2]])
    if next[1] > 0 and grid[next[0]][next[1]-1][next[2]] == state_unknown:
        addIfNotPresent(willBeOutside,[next[0], next[1]-1, next[2]])
    if next[2] < maxZ+1 and grid[next[0]][next[1]][next[2]+1] == state_unknown:
        addIfNotPresent(willBeOutside,[next[0], next[1], next[2]+1])
    if next[2] > 0 and grid[next[0]][next[1]][next[2]-1] == state_unknown:
        addIfNotPresent(willBeOutside,[next[0], next[1], next[2]-1])

surfaces = 0
for cube in filledCubes:
    if grid[cube[0]+1][cube[1]][cube[2]] == state_outside:
        surfaces += 1
    if grid[cube[0]-1][cube[1]][cube[2]] == state_outside:
        surfaces += 1
    if grid[cube[0]][cube[1]+1][cube[2]] == state_outside:
        surfaces += 1
    if grid[cube[0]][cube[1]-1][cube[2]] == state_outside:
        surfaces += 1
    if grid[cube[0]][cube[1]][cube[2]+1] == state_outside:
        surfaces += 1
    if grid[cube[0]][cube[1]][cube[2]-1] == state_outside:
        surfaces += 1

print(surfaces)