# A Rock - B Paper - C Scissors
# X Rock - Y Paper - Z Scissors

# 1 Rock - 2 Paper - 3 Scissors
# 0 Loss - 3 Draw  - 6 Win

scoretable_rps = {
    'A X\n': 1 + 3, #Rock  Rock  Draw
    'B X\n': 1 + 0, #Paper Rock  Loss
    'C X\n': 1 + 6, #Sciss Rock  Win

    'A Y\n': 2 + 6, #Rock  Paper Win
    'B Y\n': 2 + 3, #Paper Paper Draw
    'C Y\n': 2 + 0, #Sciss Paper Loss

    'A Z\n': 3 + 0, #Rock  Sciss Loss
    'B Z\n': 3 + 6, #Paper Sciss Win
    'C Z\n': 3 + 3, #Sciss Sciss Draw
}

# A Rock - B Paper - C Scissors
# X Loss - Y Draw  - Z Win

# 1 Rock - 2 Paper - 3 Scissors
# 0 Loss - 3 Draw  - 6 Win
scoretable_lwd = {
    'A X\n': 3 + 0, #Rock  Sciss Loss
    'B X\n': 1 + 0, #Paper Rock  Loss
    'C X\n': 2 + 0, #Sciss Paper Loss

    'A Y\n': 1 + 3, #Rock  Rock  Draw
    'B Y\n': 2 + 3, #Paper Paper Draw
    'C Y\n': 3 + 3, #Sciss Sciss Draw

    'A Z\n': 2 + 6, #Rock  Paper Win
    'B Z\n': 3 + 6, #Paper Sciss Win
    'C Z\n': 1 + 6, #Sciss Rock  Win
}

with open('./input.txt', 'r') as input:
    score = 0
    for line in input:
        score += scoretable_lwd[line]
    print(score)