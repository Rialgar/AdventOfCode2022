import re

state = 0
stacks = [[]]

with open('./input.txt', 'r') as input:
    for line in input:
        
        if state == 0:
            numStacks = round(len(line)/4)
            while len(stacks) < numStacks :
                stacks.append([])
            state = 1
        
        # no else, should run first time as well
        if state == 1:
            if line.startswith(' 1 '):
                state = 2
                for stack in stacks:
                    stack.reverse()
            else :
                boxes = [line[i:i+3] for i in range(0, len(line), 4)]
                for i in range(len(boxes)) :
                    char = boxes[i][1]
                    if char != ' ' :
                        stacks[i].append(char)
        elif state == 2 and len(line) > 4: #skip that empty line
            match = re.search('move (\d+) from (\d+) to (\d+)', line)
            num = int(match.group(1))
            source = int(match.group(2))
            target = int(match.group(3))
            buffer = []
            for i in range(num) :
                stacks[target-1].append(stacks[source-1].pop())            

    out = ''
    for stack in stacks :
        out += stack.pop()
    print(out)

