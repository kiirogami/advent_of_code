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


# part 2
def check_single_bad(report):
    # ugly brute force
    for remove in range(len(report)):
        cp_report = np.delete(report, remove)
        if check(cp_report) == 1:
            return 1
    else:
        return 0


safe = 0
safe_tolerance = 0
with open("data/day_02.txt", "r") as f:
    for line in f:
        row = line.strip().split(" ")
        row = np.array(row, dtype=float)
        safe += check(row)
        safe_tolerance += check_single_bad(row)
print(safe)
print(safe_tolerance)
