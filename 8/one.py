import numpy as np

firstline = True
forrest = None

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        if len(line) > 1 : #skip empty line at end of file
            row = list(map(lambda x: int(x), [line[i:i+1] for i in range(0, len(line)-1)]))
            if firstline:
                forrest = np.array(row)
                firstline = False
            else:
                forrest = np.vstack((forrest, row))

count = 0

height = forrest.shape[0]
width = forrest.shape[1]

for row in range(0, height):
    for col in range(0, width):
        if row == 0 or col == 0 or row == height-1 or col == height - 1:
            count += 1
        else:
            tree = forrest[row, col]
            check = lambda height: height < tree

            left = all(map(check, forrest[row, :col]))
            right = all(map(check, forrest[row, col+1:]))
            above = all(map(check, forrest[:row, col]))
            below = all(map(check, forrest[row+1:, col]))

            if any([left, right, above, below]) :
                count += 1

print(count)