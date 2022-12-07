with open('./input.txt', 'r') as input:
    count = 0
    for line in input:
        elves = list(map(lambda part: list(map(lambda num: int(num), part.split('-'))), line.split(','))
        )
        # -AA------
        # -----BB--

        # ------AA-
        # -BB------

        if elves[0][1] >= elves[1][0] and elves[0][0] <= elves[1][1]:
            print(elves)
            print(line)            
            count += 1

    print(count)
