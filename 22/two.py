import numpy as np

map = []
instructions = ""

readingMap = True
with open('./input.txt', 'r') as input:
    for line in input:
        if readingMap:
            if line == "\n":
                readingMap = False
            else:
                map.append(line[0: -1]) #remove \n at the end
        elif line != "\n":
            instructions = line[0:-1] #remove \n at the end

directions = [
    ('>',  1,  0),
    ('V',  0,  1),
    ('<', -1,  0),
    ('^',  0, -1),
]

y = 0
x = map[0].index('.')
d = 0

#         +---1---+---2---+
#         |       |       |
#         3       |       4
#         |       |       |
#         +-------+---5---+
#         |       |
#         6       7
#         |       |
# +---8---+-------+
# |       |       |
# 9       |       10
# |       |       |
# +-------+--11---+
# |       |
# 12      13
# |       |
# +--14---+

def wrap(target):
    right = 0
    down = 1
    left = 2
    up = 3

    if target[1] in range(0, len(map)) and target[0] in range(0, len(map[target[1]])) and map[target[1]][target[0]] != ' ':
        return (target, d)

    if(target[1] == -1 and target[0] in range(50,100) and d == up): # 1 -> 12
        return ( [0, 150 + (target[0] - 50)], right )
    elif(target[1] == -1 and target[0] in range(100,150) and d == up): # 2 -> 14
        return ( [target[0] - 100, 199], up )
    elif(target[0] == 49 and target[1] in range(0,50) and d == left): # 3 -> 9
        return ( [0, 149 - target[1]], right )
    elif(target[0] == 150 and target[1] in range(0,50) and d == right): # 4 -> 10
        return ( [99, 149 - target[1]], left )
    elif(target[1] == 50 and target[0] in range(100,150) and d == down): # 5 -> 7
        return ( [99, 50 + (target[0] - 100)], left )
    elif(target[0] == 49 and target[1] in range(50,100) and d == left): # 6 -> 8
        return ( [0 + (target[1]-50), 100], down )
    elif(target[0] == 100 and target[1] in range(50,100) and d == right): # 7 -> 5
        return ( [100 + (target[1]-50), 49], up )
    elif(target[1] == 99 and target[0] in range(0,50) and d == up): # 8 -> 6
        return ( [50, 50 + target[0]], right )
    elif(target[0] == -1 and target[1] in range(100,150) and d == left): # 9 -> 3
        return ( [50, 49 - (target[1]-100)], right )
    elif(target[0] == 100 and target[1] in range(100,150) and d == right): # 10 -> 4
        return ( [149, 49 - (target[1]-100)], left )
    elif(target[1] == 150 and target[0] in range(50,100) and d == down): # 11 -> 13
        return ( [49, 150 + (target[0] - 50)], left )
    elif(target[0] == -1 and target[1] in range(150,200) and d == left): # 12 -> 1
        return ( [50 + (target[1]-150), 0], down )
    elif(target[0] == 50 and target[1] in range(150,200) and d == right): # 13 -> 11
        return ( [50 + (target[1]-150), 149], up )
    elif(target[1] == 200 and target[0] in range(0,50) and d == down): # 14 -> 2
        return ( [100 + target[0], 0], down )
    else:
        print("UNEXPECTED WRAP LOCATION!", target, directions[d])
        return (target, d)

def step() -> bool:
    global x, y, d
    target = [x + directions[d][1], y+directions[d][2]]

    wrapped = wrap(target)
    if target != wrapped[0]:
        print('wrap', target, directions[d][0], wrapped[0], directions[wrapped[1]][0])

    target = wrapped[0]
    newDir = wrapped[1]

    if map[target[1]][target[0]] == '.':
        x = target[0]
        y = target[1]
        d = newDir
        return True
    else:
        return False

counter = 0
currentMoveString = ""

def move():
    global currentMoveString

    stepCount = int(currentMoveString)
    currentMoveString = ""
    lastStepSuccess = True
    while stepCount > 0 and lastStepSuccess:
        lastStepSuccess = step()
        stepCount -= 1

for c in instructions:
    if c in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        currentMoveString = currentMoveString + c
    else:
        move()

        if c == 'R':
            d = (d + 1) % len(directions)
        elif c == 'L':
            d = (d - 1) % len(directions)
move()

print(x, y, d)

result = (y+1) * 1000 + (x+1) * 4 + d

print(result)