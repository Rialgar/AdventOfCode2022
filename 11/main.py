from typing import Callable
import math

monkeys: list['Monkey'] = []

class Monkey:
    modulus = 1

    def __init__(
        self,
        items: list[int],
        operation: Callable[[int], int],
        testNum: int,
        targetTrue: int,
        targetFalse: int
    ) -> None:
        self.items = items
        self.operation = operation
        self.testNum = testNum
        self.targetTrue = targetTrue
        self.targetFalse = targetFalse
        self.counter = 0

        Monkey.modulus *= testNum

    def play(self):
        for item in self.items:
            item = self.operation(item)
            #item = math.floor(item/3) #removed for part 2
            item = item % Monkey.modulus #added for part 2, but should not break part 1
            if (item % self.testNum) == 0 :
                monkeys[self.targetTrue].items.append(item)
            else:
                monkeys[self.targetFalse].items.append(item)
            self.counter += 1

        self.items = []

def playRound():
    for monkey in monkeys:
        monkey.play()

def parseMonkey(lines: list[str]) -> Monkey:
    itemstart = len('  Starting items: ')
    items = list(map(lambda s: int(s), lines[0][itemstart:-1].split(', ')))
    
    operationstart = len('  Operation: new = old ')
    operator = lines[1][operationstart:operationstart+1]
    operand = lines[1][operationstart+2:-1]
    operation: Callable[[int], int] = lambda a: a
    if operator == '+' :
        operand = int(operand)
        operation = lambda a: a + operand
    elif operator == '*' :
        if operand == 'old':
            operation = lambda a: a * a
        else:
            operand = int(operand)
            operation = lambda a: a * operand
    else:
        raise 'unsupported operation ' + operation

    teststart = len('  Test: divisible by ')
    testnum = int(lines[2][teststart:-1])

    targetTrueStart = len('    If true: throw to monkey ')
    targetTrue = int(lines[3][targetTrueStart:-1])

    targetFalseStart = len('    If false: throw to monkey ')
    targetFalse = int(lines[4][targetFalseStart:-1])

    return Monkey(items, operation, testnum, targetTrue, targetFalse)

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    buffer = []
    for line in input:
        if line.startswith('Monkey') :

            buffer = []
        else:
            buffer.append(line)
            if line.startswith('    If false') :
                monkeys.append(parseMonkey(buffer))

#for i in range(20): # part one
for i in range(10000): # part two
    playRound()

byCounter = sorted(monkeys, key=lambda monkey: monkey.counter, reverse=True)

print(byCounter[0].counter*byCounter[1].counter)

    