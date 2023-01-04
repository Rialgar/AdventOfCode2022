import numpy as np

map = []
instructions = ""

readingMap = True
with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
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

def step() -> bool:
    global x, y
    target = [x + directions[d][1], y+directions[d][2]]
    if directions[d][0] == '>':
        if target[0] >= len(map[target[1]]) or map[target[1]][target[0]] == ' ':
            target[0] = min(map[target[1]].index('.'), map[target[1]].index('#'))
    elif directions[d][0] == '<':
        if target[0] < 0 or map[target[1]][target[0]] == ' ':
            target[0] = max(map[target[1]].rindex('.'), map[target[1]].rindex('#'))
    elif directions[d][0] == 'V':
        if target[1] >= len(map) or target[0] >= len(map[target[1]]) or map[target[1]][target[0]] == ' ':
            for possibleY in range(len(map)):
                if target[0] < len(map[possibleY]) and map[possibleY][target[0]] != ' ':
                    target[1] = possibleY
                    break
    elif directions[d][0] == '^':
        if target[1] < 0 or target[0] >= len(map[target[1]]) or map[target[1]][target[0]] == ' ':
            for index in range(len(map)):
                possibleY = len(map) - 1 - index
                if target[0] < len(map[possibleY]) and map[possibleY][target[0]] != ' ':
                    target[1] = possibleY
                    break
    if map[target[1]][target[0]] == '.':
        x = target[0]
        y = target[1]
        #print('Moved', directions[d][0])
        return True
    else:
        #print('wall', directions[d][0])
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