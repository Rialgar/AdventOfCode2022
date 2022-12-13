import functools

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

lines = []

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:        
        if len(line) > 1: #disregard empty lines
            lines.append(eval(line))
sep_2 = [[2]]
sep_6 = [[6]]

lines.append(sep_2)
lines.append(sep_6)

lines.sort(key=functools.cmp_to_key(compare))

print(lines.index(sep_2)+1)
print(lines.index(sep_6)+1)
print((lines.index(sep_2)+1) * (lines.index(sep_6)+1))