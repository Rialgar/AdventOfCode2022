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

maxScore = 0

height = forrest.shape[0]
width = forrest.shape[1]

for row in range(0, height):
    for col in range(0, width):
        if not (row == 0 or col == 0 or row == height-1 or col == height - 1):
            tree = forrest[row, col]        

            def viewDistance(list):
                return next((index+1 for index, item in enumerate(list) if item >= tree), len(list))
            
            left = viewDistance(forrest[row, :col][::-1])
            right = viewDistance(forrest[row, col+1:])
            above = viewDistance(forrest[:row, col][::-1])
            below = viewDistance(forrest[row+1:, col])

            score = left*right*above*below
            maxScore = max(maxScore, score)

print(maxScore)
            