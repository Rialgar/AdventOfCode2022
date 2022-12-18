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
grid = []
for x in range(maxX+2):
    grid.append([])
    for y in range(maxY+2):
        grid[x].append([])
        for z in range(maxZ+2):
            grid[x][y].append(False)

for cube in filledCubes:
    grid[cube[0]][cube[1]][cube[2]] = True

surfaces = 0
for cube in filledCubes:
    if not grid[cube[0]+1][cube[1]][cube[2]]:
        surfaces += 1
    if not grid[cube[0]-1][cube[1]][cube[2]]:
        surfaces += 1
    if not grid[cube[0]][cube[1]+1][cube[2]]:
        surfaces += 1
    if not grid[cube[0]][cube[1]-1][cube[2]]:
        surfaces += 1
    if not grid[cube[0]][cube[1]][cube[2]+1]:
        surfaces += 1
    if not grid[cube[0]][cube[1]][cube[2]-1]:
        surfaces += 1

print(surfaces)