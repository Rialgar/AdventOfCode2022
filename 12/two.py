map = []

y = 0
goal = (0, 0)

class Path:

    def __init__(self, location, pathSoFar: list) -> None:
        self.location = location
        self.path = pathSoFar.copy()
        self.path.append(self.location)
        y = self.location[0]
        x = self.location[1]
        self.height = map[y][x]

    def isGoal(self):
        return self.location == goal

starts = []

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:        
        x = 0
        map.append([])
        for char in line:
            if(char == '\n'):
                continue
            if char == 'S':
                char = 'a'
            elif char == 'E':
                char = 'z'
                goal = (y, x)

            if char == 'a':
                starts.append((y, x))

            map[y].append(ord(char) - ord('a'))
            x += 1
        y += 1
            
def findPathLength(start):
    checked = []

    for y in range(len(map)):
        checked.append([])
        for x in range(len(map[y])):
            checked[y].append(False)

    checked[start[0]][start[1]] = True
    queue = [Path(start, [])]
    neighbours = [
        ( 0,-1),
        ( 0, 1),
        (-1, 0),
        ( 1, 0),
    ]

    while len(queue)>0 and not(queue[0].isGoal()):
        next = queue[0]
        queue = queue[1:]
        for n in neighbours:
            y = next.location[0] + n[0]
            x = next.location[1] + n[1]
            if y >= 0 and y < len(map) and x >= 0 and x < len(map[y]) and not(checked[y][x]) and map[y][x] <= next.height+1:
                queue.append(Path((y, x), next.path))
                checked[y][x] = True

    if len(queue) > 0:
        return queue[0].path #changed after submission to get the visual map, originally I just kept the length and used 500 as a save 'too big' value
    else:
        return []

short = []
for start in starts:
    next = findPathLength(start)
    if len(next) > 0 and (len(short) == 0 or len(next)<len(short)):
        short = next

print(len(short))

# did this after part two, but I just wanted to see the path we found
for y in range(len(map)):
    for x in range(len(map[y])):
        if (y, x) in short:
            print('\u001b[44m' + chr(ord('a')+map[y][x]) + '\u001b[0m', end='')
        else:
            print(chr(ord('a')+map[y][x]), end='')
    print('')