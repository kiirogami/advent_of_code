import numpy as np

PATH = "data/day_01.txt"


def part1(data):
    dial = 50
    solution = 0
    for e in data:
        dial = dial + int(e[1:]) if "R" in e else dial - int(e[1:])
        dial %= 100
        if dial == 0:
            solution += 1
    return solution


def part2(data):
    dial = 50
    solution = 0
    for e in data:
        dial = dial + int(e[1:]) if "R" in e else dial - int(e[1:])
        if dial <= 0 or dial >= 100:
            solution += np.sign(dial) * (dial // 100)
        dial %= 100
    return solution


if __name__ == "__main__":
    data = np.loadtxt(PATH, dtype=str)
    print(f"part1: {part1(data)}")
    print(f"part2: {part2(data)}")
