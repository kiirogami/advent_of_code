import numpy as np
import itertools
import time

FILE_PATH = "data/day_07.txt"

PART_2 = True


def main():
    time_start = time.time()
    result = 0
    with open(FILE_PATH, "r") as f:
        for line in f:
            row = line.strip()
            a, b = np.array(row.split(": "))
            b = np.array(b.split(" "), dtype=int)
            a = int(a)
            if check_calibrations(a, b, PART_2):
                result += a
    time_end = time.time()
    print(result)
    print(time_end - time_start, "s")


def check_calibrations(a, b, part_2=False):
    if part_2:
        perms = list(itertools.product([-1, 0, 1], repeat=len(b) - 1))
    else:
        perms = list(itertools.product([0, 1], repeat=len(b) - 1))
    for p in perms:
        value = b[0]
        for i in range(1, len(b)):
            if p[i - 1] == 0:
                value += b[i]
            elif p[i - 1] == 1:
                value *= b[i]
            elif p[i - 1] == -1:
                digs = len(str(b[i]))
                value = value * 10**digs + b[i]
            if value > a:
                break
        else:
            if value == a:
                return True
    else:
        return False


if __name__ == "__main__":
    main()
