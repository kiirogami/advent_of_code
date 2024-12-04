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


def check_single_bad(report):
    if report[0] > report[1]:
        report = report[::-1]
    # sooo ugly, tried with removing single bad level and recursion, couldnt make it work
    for remove in range(len(report)):
        cp_report = np.delete(report, remove)
        for i in range(0, len(cp_report) - 1):
            if (cp_report[i + 1] - cp_report[i]) >= 1 and (cp_report[i + 1] - cp_report[i]) <= 3:
                continue
            else:
                break
        else:
            return 1
    else:
        return 0


safe = 0
safe_tolerance = 0
with open("input.txt", "r") as f:
    for line in f:
        row = line.strip().split(" ")
        row = np.array(row, dtype=float)
        safe += check(row)
        safe_tolerance += check_single_bad(row)
print(safe)
print(safe_tolerance)
