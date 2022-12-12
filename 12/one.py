map = []
checked = []

y = 0
start = (0, 0)
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

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:        
        x = 0
        map.append([])
        checked.append([])
        for char in line:
            if(char == '\n'):
                continue

            checked[y].append(False)
            if char == 'S':
                char = 'a'
                start = (y, x)
                checked[y][x] = True
            elif char == 'E':
                char = 'z'
                goal = (y, x)
            map[y].append(ord(char) - ord('a'))
            x += 1
        y += 1
            

queue = [Path(start, [])]
neighbours = [
    ( 0,-1),
    ( 0, 1),
    (-1, 0),
    ( 1, 0),    
]


while not(queue[0].isGoal()):
    next = queue[0]
    queue = queue[1:]
    for n in neighbours:
        y = next.location[0] + n[0]
        x = next.location[1] + n[1]
        if y >= 0 and y < len(map) and x >= 0 and x < len(map[y]) and not(checked[y][x]) and map[y][x] <= next.height+1:
            queue.append(Path((y, x), next.path))
            checked[y][x] = True

print(len(queue[0].path) - 1)

# did this after part two, but I just wanted to see the path we found
for y in range(len(map)):
    for x in range(len(map[y])):
        if (y, x) in queue[0].path:
            print('\u001b[44m' + chr(ord('a')+map[y][x]) + '\u001b[0m', end='')
        else:
            print(chr(ord('a')+map[y][x]), end='')
    print('')