def addTuples(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]: return (a[0]+b[0], a[1]+b[1])
def subTuples(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]: return (a[0]-b[0], a[1]-b[1])

def follow(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
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

knots = [(0,0) for i in range(10)]

visited = {(0,0)}

with open('./input.txt', 'r') as input:
#with open('./example2.txt', 'r') as input:
    for line in input:
        if len(line) > 1 : #skip empty line at end of file
            direction = directions[line[0]]
            steps = int(line[2:-1])
            for i in range(0, steps):
                knots[0] = addTuples(knots[0], direction)
                for j in range(len(knots)-1):
                    knots[j+1] = follow(knots[j], knots[j+1])
                visited.add(knots[-1])

print(len(visited))
