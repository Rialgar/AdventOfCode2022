def unique(str):
    for i in range(len(str)):
        for j in range(i+1, len(str)):
            if(str[i] == str[j]):
                return False
    return True

with open('./input.txt', 'r') as input:
    line = input.read()
    for i in range(len(line)-14):
        if unique(line[i:i+14]):
            print(i+14, line[i:i+14])
            break
