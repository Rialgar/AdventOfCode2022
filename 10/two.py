cycle = 0
register_value = 1
out = ''

def advance():
    global cycle, out
    gridpos = cycle % 40
    if gridpos >= register_value-1 and gridpos <= register_value +1 :
        out += '#'
    else:
        out += ' ' #much more legible than using .

    cycle += 1
    if cycle % 40 == 0 :
        out += '\n'


with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        if line.startswith('noop'):
            advance()
        if line.startswith('addx'):
            change = int(line[5:-1])
            advance()
            advance()
            register_value += change            

print(out)
