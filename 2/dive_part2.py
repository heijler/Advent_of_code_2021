import operator

print("Day 2: Dive! Part 2")

aim = 0


def getInput():
    with open("2/input.txt") as f:
        return f.read().splitlines()


def parseInput(input):
    direction, amount = input.split(" ")
    amount = int(amount)
    global aim

    if direction == "forward":
        return amount, aim * amount
    if direction == "down":
        aim += amount
    if direction == "up":
        aim -= amount
    return 0, 0


def dive():
    coordinate = 0, 0

    for instruction in getInput():
        coordinate = tuple(map(operator.add, coordinate, parseInput(instruction)))

    x, y = coordinate
    print("P2 Final coordinates: " + str(coordinate))
    print("P2 Final aim: " + str(aim))
    print("P2 Final coordinate product: " + str(x * y))


dive()
