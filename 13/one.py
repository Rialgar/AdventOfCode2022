sum = 0
index = 1
step = 0

def compare(a, b):
    if type(a) == list:
        if type(b) != list:
            return compare(a, [b])
        else:
            for i in range(min(len(a), len(b))):
                comp = compare(a[i], b[i])
                if comp != 0:
                    return comp
            return len(a) - len(b)

    elif type(b) == list:
        return compare([a], b)
    else:
        return a-b

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    left = []
    right = []
    for line in input:        
        if step == 0:
            left = eval(line)
        elif step == 1:
            right = eval(line)
            if compare(left, right) <= 0:
                sum += index
        else:
            index += 1
        step = (step + 1) % 3

print(sum)