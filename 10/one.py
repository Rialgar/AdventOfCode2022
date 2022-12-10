cycle = 0
register_value = 1
sum = 0

def advance():
    global cycle, sum
    cycle += 1
    if (cycle+20) % 40 == 0 :
        sum += cycle*register_value
        print(cycle, register_value, cycle*register_value, sum)


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