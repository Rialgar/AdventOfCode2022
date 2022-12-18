top = -1

class Shape:
    def __init__(self, map: list[list[bool]]) -> None:
        self.y = top + 4
        self.x = 2
    
    def shift(self, map: list[list[bool]], direction: int) -> None:
        if not self.collides(map, direction, 0):
            self.x += direction

    def fall(self, map: list[list[bool]]) -> bool:
        if self.collides(map, 0, -1):
            self.persist(map)
            return False
        else:
            self.y -= 1
            return True
    
    def collides(self, map: list[list[bool]], dx:int, dy:int) -> bool:
        return False

    def persist(self, map: list[list[bool]]) -> None:
        pass

class HorizontalLine(Shape):
    def collides(self, map: list[list[bool]], dx:int, dy:int) -> bool:
        x = self.x + dx
        y = self.y + dy
        while len(map) < y+1:
            map.append([False, False, False, False, False, False, False])
        return y < 0 or x < 0 or x+3 > 6 or map[y][x] or map[y][x+1] or map[y][x+2] or map[y][x+3]

    def persist(self, map: list[list[bool]]) -> None:
        x = self.x
        y = self.y
        while len(map) < y+1:
            map.append([False, False, False, False, False, False, False])
        map[y][x] = True
        map[y][x+1] = True
        map[y][x+2] = True
        map[y][x+3] = True

class Cross(Shape):
    def collides(self, map: list[list[bool]], dx:int, dy:int) -> bool:
        x = self.x + dx
        y = self.y + dy
        while len(map) < y+3:
            map.append([False, False, False, False, False, False, False])

        return y < 0 or x < 0 or x+2 > 6 or map[y][x+1] or map[y+1][x] or map[y+1][x+1] or map[y+1][x+2] or map[y+2][x+1]

    def persist(self, map: list[list[bool]]) -> None:
        x = self.x
        y = self.y
        while len(map) < y+3:
            map.append([False, False, False, False, False, False, False])

        map[y][x+1] = True
        map[y+1][x] = True
        map[y+1][x+1] = True
        map[y+1][x+2] = True
        map[y+2][x+1] = True

class Corner(Shape):
    def collides(self, map: list[list[bool]], dx:int, dy:int) -> bool:
        x = self.x + dx
        y = self.y + dy
        while len(map) < y+3:
            map.append([False, False, False, False, False, False, False])

        return y < 0 or x < 0 or x+2 > 6 or map[y][x] or map[y][x+1] or map[y][x+2] or map[y+1][x+2] or map[y+2][x+2]

    def persist(self, map: list[list[bool]]) -> None:
        x = self.x
        y = self.y
        while len(map) < y+3:
            map.append([False, False, False, False, False, False, False])

        map[y][x] = True
        map[y][x+1] = True
        map[y][x+2] = True
        map[y+1][x+2] = True
        map[y+2][x+2] = True

class VerticalLine(Shape):
    def collides(self, map: list[list[bool]], dx:int, dy:int) -> bool:
        x = self.x + dx
        y = self.y + dy
        while len(map) < y+4:
            map.append([False, False, False, False, False, False, False])

        return y < 0 or x < 0 or x > 6 or map[y][x] or map[y+1][x] or map[y+2][x] or map[y+3][x]

    def persist(self, map: list[list[bool]]) -> None:
        x = self.x
        y = self.y
        while len(map) < y+4:
            map.append([False, False, False, False, False, False, False])

        map[y][x] = True
        map[y+1][x] = True
        map[y+2][x] = True
        map[y+3][x] = True

class Box(Shape):
    def collides(self, map: list[list[bool]], dx:int, dy:int) -> bool:
        x = self.x + dx
        y = self.y + dy
        while len(map) < y+2:
            map.append([False, False, False, False, False, False, False])

        return y < 0 or x < 0 or x+1 > 6 or map[y][x] or map[y+1][x] or map[y][x+1] or map[y+1][x+1]

    def persist(self, map: list[list[bool]]) -> None:
        x = self.x
        y = self.y
        while len(map) < y+4:
            map.append([False, False, False, False, False, False, False])

        map[y][x] = True
        map[y+1][x] = True
        map[y][x+1] = True
        map[y+1][x+1] = True

shapes: list[Shape] = [HorizontalLine, Cross, Corner, VerticalLine, Box]

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        movementSequence = line[:-1] # remove line ending
        break

shapeIndex = 0
movementIndex = 0

directions = {
    '<' : -1,
    '>' : 1
}

def printMap(map, shape):
    for y in range(len(map)-1, -1, -1):
        for x in range(0, len(map[y])):
            if(map[y][x]):
                print('#', end='')
            else:
                print('.', end='')
        print()

map = []
currentShape: Shape = shapes[shapeIndex](map)
while shapeIndex < 2022:
    direction = directions[movementSequence[movementIndex]]
    #print(movementSequence[movementIndex])
    if not currentShape.collides(map, direction, 0):
        currentShape.x += direction
    movementIndex = (movementIndex + 1) % len(movementSequence) 
    if not currentShape.fall(map):
        top = len(map)-1
        while not (map[top][0] or map[top][1] or map[top][2] or map[top][3] or map[top][4] or map[top][5] or map[top][6]):
            top -= 1

        shapeIndex += 1
        currentShape = shapes[shapeIndex % len(shapes)](map)
        print(shapeIndex)

#printMap(map, None)

print()
print(top+1)