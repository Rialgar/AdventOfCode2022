import re

operations = {
    '+': lambda a,b: a+b,
    '-': lambda a,b: a-b,
    '*': lambda a,b: a*b,
    '/': lambda a,b: a/b,
}

operationsFindA = {
    '+': lambda result, b: result - b,
    '-': lambda result, b: result + b,
    '*': lambda result, b: result / b,
    '/': lambda result, b: result * b,
}

operationsFindB = {
    '+': lambda result, a: result - a,
    '-': lambda result, a: a - result,
    '*': lambda result, a: result / a,
    '/': lambda result, a: a / result,
}

monkeys = dict()

class Monkey:
    def __init__(self, name, operation=None, a=None, b=None, value = None) -> None:
        self.name = name

        self.operation = operation
        self.a = a
        self.b = b
        self.value = value

        self.aValue = None
        self.bValue = None
        self.operationResult = None

        self.usedBy = None

    def __str__(self) -> str:
        if self.operation != None:
            return self.a + ' ' + self.operation + ' ' + self.b
        else:
            return str(self.value)

    def link(self) -> None:
        if self.operation != None:
            a = monkeys[self.a]
            if a.usedBy != None:
                raise 'Used multiple times!'
            a.usedBy = self.name
            b = monkeys[self.b]
            if b.usedBy != None:
                raise 'Used multiple times!'
            b.usedBy = self.name

    def getValue(self):
        if self.name == 'humn':
            self.value = monkeys[self.usedBy].getChildValue(self.name)

        if self.value != None:
            return self.value
        
        if self.operation:
            if self.operationResult == None:
                aValue = monkeys[self.a].getValue()
                bValue = monkeys[self.b].getValue()
                if(aValue != None and bValue != None):
                    self.aValue = aValue
                    self.bValue = bValue
                    self.operationResult = operations[self.operation](aValue, bValue)
            return self.operationResult

    def getChildValue(self, child):
        if child == self.a:
            return self.getAValue()
        if child == self.b:
            return self.getBValue()

    def getAValue(self):
        if self.aValue == None:
            if self.operationResult == None:
                self.operationResult = monkeys[self.usedBy].getChildValue(self.name)
            self.bValue = monkeys[self.b].getValue()
            self.aValue = operationsFindA[self.operation](self.operationResult, self.bValue)
        return self.aValue

    def getBValue(self):
        if self.bValue == None:
            if self.operationResult == None:
                self.operationResult = monkeys[self.usedBy].getChildValue(self.name)
            self.aValue = monkeys[self.a].getValue()
            self.bValue = operationsFindB[self.operation](self.operationResult, self.aValue)
        return self.bValue

expressionWithValue = re.compile('([a-z]{4}): ([0-9]+)')
expressionWithOperation = re.compile('([a-z]{4}): ([a-z]{4}) ([+\-*/]) ([a-z]{4})')

with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        matchWithValue = expressionWithValue.match(line)
        if matchWithValue != None:
            name = matchWithValue.group(1)
            if name == 'humn':
                monkeys['humn'] = Monkey(name='humn')
            else:
                monkeys[name] = Monkey(name=name, value=int(matchWithValue.group(2)))
        else:
            matchWithOperation = expressionWithOperation.match(line)
            name = matchWithOperation.group(1)
            a = matchWithOperation.group(2)
            b = matchWithOperation.group(4)
            if name == 'root':
                monkeys['root'] = Monkey(name='root', operation = '-', a=a, b=b)
                monkeys['root'].operationResult = 0
            else:
                operation = matchWithOperation.group(3)
                monkeys[name] = Monkey(name=name, operation=operation, a=a, b=b)

for key in monkeys:
    monkeys[key].link()

print(monkeys['humn'].getValue())