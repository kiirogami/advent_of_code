from scipy.optimize import linprog
import numpy as np
import re

FILE = "data/day_13_test.txt"
FILE = "data/day_13.txt"

PART_2 = True


def main():
    pattern = r"[XY][+=](-?\d+)"
    a = []
    b = []
    target = []
    total_cost = 0
    with open(FILE, "r") as file:
        for line in file:
            row = line.strip()
            matches = re.findall(pattern, row)
            numbers = list(map(int, matches))
            if "A" in row:
                a = numbers
            elif "B" in row:
                b = numbers
            elif "Prize" in row:
                target = numbers
                if not PART_2:
                    a_amount, b_amount, cost = LP_result(a, b, target)
                    if cost is None or a_amount > 100 or b_amount > 100:
                        continue
                    else:
                        total_cost += cost
                else:
                    target = np.asarray(target, dtype=np.float64)
                    target = target + np.array(
                        [10000000000000, 10000000000000], dtype=np.float64
                    )
                    a_amount, b_amount, cost = LP_result(a, b, target)
                    if cost is None:
                        pass
                    else:
                        total_cost += cost
            elif row == "":
                continue
    print(total_cost)


def LP_result(a_press, b_press, target):
    costs = np.array([3, 1], dtype=np.float64)
    A = np.vstack((a_press, b_press), dtype=np.float64).T
    b = np.asarray(target, dtype=np.float64)

    bounds = [(0, None), (0, None)]  # positive a_amount and b_amount

    # result = linprog(
    #     c=costs,
    #     A_eq=A,
    #     b_eq=b,
    #     bounds=bounds,
    #     method="highs",
    #     integrality=[1, 1],  # int result
    # )

    result_2 = np.linalg.solve(A, b)
    result_2 = np.round(result_2, 2)

    if np.array_equal(result_2 % 1, [0, 0]) and all(result_2 >= 0):
        return (result_2[0], result_2[1], np.sum(result_2 * costs))
    else:
        return (None, None, None)

    if result.success:
        return (result.x[0], result.x[1], result.fun)
    else:
        return (None, None, None)


if __name__ == "__main__":
    main()
    70179294109316
    65872475396210
    92871736253789
