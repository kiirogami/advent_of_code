import numpy as np
from collections import deque

PATH = "data/day_11_easy.txt"
PATH = "data/day_11.txt"


def main():
    data = np.genfromtxt(PATH, dtype=str, delimiter=":")
    dict = {}
    for row in data:
        dict[row[0]] = row[-1].split()

    solution1 = part1(dict)
    print(solution1)


def part1(dict):
    start = "you"
    goal = "out"

    memo = {}

    # little bit of vibe coding
    def count_paths(current_device):
        if current_device == goal:
            return 1

        if current_device in memo:
            return memo[current_device]

        total_paths = 0

        for next_device in dict[current_device]:
            total_paths += count_paths(next_device)

        memo[current_device] = total_paths
        return total_paths

    return count_paths(start)


def part2(lights):
    pass


if __name__ == "__main__":
    main()
