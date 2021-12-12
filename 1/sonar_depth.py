print("Day 1: Sonar Sweep Part 1 & 2")


def getInput():
    with open("1/input.txt") as f:
        return f.read().splitlines()


def part_one():
    counter = 0
    prev_measurement = None
    for measurement in getInput():
        measurement = int(measurement)
        if prev_measurement is not None and measurement > prev_measurement:
            counter += 1
        prev_measurement = measurement
    print("P1 Depth increased count: " + str(counter))


def part_two():
    counter = 0
    prev_measurement = None
    for index, value in enumerate(getInput()):
        if index + 2 < len(getInput()):
            sum = int(value) + int(getInput()[index + 1]) + int(getInput()[index + 2])
            if prev_measurement is not None and sum > prev_measurement:
                counter += 1
            prev_measurement = sum
    print("P2 Depth increased count: " + str(counter))


part_one()
part_two()
