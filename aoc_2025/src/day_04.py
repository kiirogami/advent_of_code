import numpy as np
from scipy.ndimage import convolve

PATH = "data/day_04_easy.txt"
PATH = "data/day_04.txt"


def part2(data):
    result, rolls = part1(data)

    if result == 0:
        return 0

    return result + part2(rolls)


def part1(data):
    if data.dtype != bool:
        rolls = data == "@"
    else:
        rolls = data

    binary_mask = np.array(rolls, dtype=int)
    kernel = np.full((3, 3), 1)
    kernel[1, 1] = 0
    # use convolution to count neighbours using binary mask and kernel filled with 1
    neighbours_amount = convolve(binary_mask, kernel, mode="constant", cval=0)
    accessable = neighbours_amount < 4

    accessable_roll = accessable & rolls
    solution = np.sum(accessable_roll)
    rolls[accessable_roll] = False

    return solution, rolls


if __name__ == "__main__":
    data = np.genfromtxt(PATH, dtype=str, delimiter=1)
    print(f"part1: {part1(np.copy(data))[0]}")
    print(f"part2: {part2(np.copy(data))}")
