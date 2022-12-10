def addTuples(a, b): return (a[0]+b[0], a[1]+b[1])
def subTuples(a, b): return (a[0]-b[0], a[1]-b[1])

def follow(head, tail):
    delta = subTuples(head, tail)
    x = 0
    y = 0
    
    if abs(delta[0]) == 2 or (abs(delta[0]) == 1 and abs(delta[1]) == 2):
        x = int(delta[0]/abs(delta[0]))
    
    if abs(delta[1]) == 2 or (abs(delta[1]) == 1 and abs(delta[0]) == 2):
        y = int(delta[1]/abs(delta[1]))

    return addTuples(tail, (x,y))


directions = {
    "U": ( 0, 1),
    "D": ( 0,-1),
    "L": (-1, 0),
    "R": ( 1, 0),
}

head = (0,0)
tail = (0,0)

visited = {tail}

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        if len(line) > 1 : #skip empty line at end of file
            direction = directions[line[0]]
            steps = int(line[2:-1])
            for i in range(0, steps):
                head = addTuples(head, direction)
                tail = follow(head, tail)
                visited.add(tail)

print(len(visited))
