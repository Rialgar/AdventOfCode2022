def unique(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if(str[i] == str[j]):
                return False
    return True

with open('./input.txt', 'r') as input:
    line = input.read()
    for i in range(len(line)-4):
        if unique(line[i:i+4]):
            print(i+4, line[i:i+4])
            break
