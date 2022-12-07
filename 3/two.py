ord_a = ord('a');
ord_A = ord('A');

def priority(char):
    ord_char = ord(char);
    if ord_char >= ord_a:
        return ord_char - ord_a + 1
    else:
        return ord_char - ord_A + 27

with open('./input.txt', 'r') as input:
    sum = 0
    lines = []
    for line in input:
        lines.append(line)
        if len(lines) == 3:
            for char in lines[0]:
                if (char in lines[1]) and (char in lines[2]):
                    sum += priority(char)
                    break
            lines = []

    print(sum)