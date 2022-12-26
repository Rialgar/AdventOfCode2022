numbers = []
orderToCall = []

counter = 0
with open('./input.txt', 'r') as input:
#with open('./example.txt', 'r') as input:
    for line in input:
        if len(line) > 0:
            numbers.append(int(line))
            orderToCall.append(counter)
            counter = counter + 1

length = len(numbers)

def move(orderToMove):
    global numbers
    global orderToCall

    index = orderToCall.index(orderToMove)

    numberToMove = numbers[index]
    target = (index + numberToMove)
    while target > length-1:
        target -= length-1
    while target <= 0:
        target += length-1

    if target < index:
        numbers = numbers[:target] + [numberToMove] + numbers[target:index] + numbers[index+1:]
        orderToCall = orderToCall[:target] + [orderToMove] + orderToCall[target:index] + orderToCall[index+1:]
    elif target > index:
        numbers = numbers[:index] + numbers[index+1:target+1] + [numberToMove] + numbers[target+1:]
        orderToCall = orderToCall[:index] + orderToCall[index+1:target+1] + [orderToMove] + orderToCall[target+1:]

for i in range(length):
    move(i)

zeroIndex = numbers.index(0)

indexOne = (zeroIndex + 1000) % length
indexTwo = (zeroIndex + 2000) % length
indexThree = (zeroIndex + 3000) % length
print(numbers[indexOne], numbers[indexTwo], numbers[indexThree], numbers[indexOne] + numbers[indexTwo] + numbers[indexThree])