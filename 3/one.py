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
    for line in input:
        length = len(line)-1 #acounting for /n
        mid = round(length/2)
        left = line[:mid]
        right = line[mid:-1]

        error = ''
        for char in left:
            if char in right :
                error = char
                break

        sum += priority(error)

    print(sum)
