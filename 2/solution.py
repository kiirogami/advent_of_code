import numpy as np


def check(report):
    if report[0] > report[1]:
        report = report[::-1]

    di = report[0]
    for i in range(1, len(report)):
        if (report[i] - di) >= 1 and (report[i] - di) <= 3:
            di = report[i]
        else:
            return 0
    else:
        return 1


safe = 0
with open("input.txt", "r") as f:
    for line in f:
        row = line.strip().split(" ")
        row = np.array(row, dtype=float)
        safe += check(row)
print(safe)
