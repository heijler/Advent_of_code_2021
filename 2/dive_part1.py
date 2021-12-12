import operator

print("Day 2: Dive! Part 1")


def getInput():
    with open("2/input.txt") as f:
        return f.read().splitlines()


def parseInput(input):
    direction, amount = input.split(" ")
    amount = int(amount)

    if direction == "forward":
        return amount, 0
    if direction == "down":
        return 0, amount
    if direction == "up":
        return 0, -amount


def dive():
    coordinate = 0, 0
    for instruction in getInput():
        coordinate = tuple(map(operator.add, coordinate, parseInput(instruction)))

    x, y = coordinate
    print("P1 Final coordinates: " + str(coordinate))
    print("P1 Final coordinate product: " + str(x * y))


dive()
