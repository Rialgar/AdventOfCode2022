minX = 500
maxX = 500

maxDepth = 0

paths = []

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        path = []
        for pointString in line.split('->'):
            coords = pointString.split(',')
            point = (int(coords[0]), int(coords[1]))
            path.append(point)
            minX = min(minX, point[0])
            maxX = max(maxX, point[0])
            maxDepth = max(maxDepth, point[1])
        paths.append(path)

map = []
for depth in range(maxDepth+1):
    map.append([])
    for x in range(minX, maxX+1):
        if(depth == 0 and x == 500):
            map[depth].append('*')
        else:
            map[depth].append('.')
    
def printMap():
    for depth in range(maxDepth+1):
        for x in range(minX, maxX+1):
            print(map[depth][x-minX], end='')
        print()
    print()

def getMap(x, y):
    if x < minX or x > maxX or y > maxDepth:
        return '.'
    else:
        return map[y][x-minX]


def setMap(x, y, value):
    map[y][x-minX] = value


for path in paths:
    for i in range(len(path)-1):
        print(i, path[i], path[i+1])
        
        startX = min(path[i][0], path[i+1][0])
        endX = max(path[i][0], path[i+1][0])

        startY = min(path[i][1], path[i+1][1])
        endY = max(path[i][1], path[i+1][1])
        
        for x in range(startX, endX+1):
            for y in range(startY, endY+1):
                setMap(x, y, '#')

done = False
counter = 0
while not done:
    sand = [500,0]
    falling = True
    
    while falling:
        if sand[1] > maxDepth:
            falling = False
        elif getMap(sand[0], sand[1]+1) == '.':
            sand[1] += 1
        elif getMap(sand[0]-1, sand[1]+1) == '.':
            sand[0] -= 1
            sand[1] += 1
        elif getMap(sand[0]+1, sand[1]+1) == '.':
            sand[0] += 1
            sand[1] += 1
        else:
            falling = False
    if sand[0] < minX or sand[0] > maxX or sand[1] > maxDepth:
        done = True
    else:
        counter += 1
        setMap(sand[0], sand[1], 'o')

    printMap()    

print(counter)