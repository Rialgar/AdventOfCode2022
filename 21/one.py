import re

monkeys = dict()

class Monkey:
    def __init__(self, operation=None, a=None, b=None, value = None) -> None:
        self.operation = operation
        self.a = a
        self.b = b
        self.value = value
        pass

    def __str__(self) -> str:
        if self.operation != None:
            return self.a + ' ' + self.b
        else:
            return str(self.value)

    def getValue(self):
        if self.value == None:
            a = monkeys[self.a]
            b = monkeys[self.b]
            self.value = self.operation(a.getValue(), b.getValue())
        return self.value

def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b
operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div
}

expressionWithValue = re.compile('([a-z]{4}): ([0-9]+)')
expressionWithOperation = re.compile('([a-z]{4}): ([a-z]{4}) ([+\-*/]) ([a-z]{4})')

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        matchWithValue = expressionWithValue.match(line)
        if matchWithValue != None:
            monkeys[matchWithValue.group(1)] = Monkey(value=int(matchWithValue.group(2)))
        else:
            matchWithOperation = expressionWithOperation.match(line)
            operation = operations[matchWithOperation.group(3)]
            a = matchWithOperation.group(2)
            b = matchWithOperation.group(4)
            monkeys[matchWithOperation.group(1)] = Monkey(operation=operation, a=a, b=b)

print(monkeys['root'].getValue())