import numpy as np
import re

PATH = "data/day_06_easy.txt"
PATH = "data/day_06.txt"


def part2(numbers, operators):
    numbers = np.copy(numbers)
    numbers = cephalopod_transform(numbers)
    result = part1(numbers, operators)
    return result


def cephalopod_transform(numbers):
    # transpose
    num_len = numbers.shape[0]

    numbers = np.array(np.copy(numbers), dtype=str)

    cephalopod_numbers = np.zeros_like(numbers, dtype=int)

    cephalopod_numbers = [[] for _ in range(num_len)]

    for c in range(numbers.shape[1]):
        column = np.copy(numbers[:, c])
        column = column.view("<U1").reshape(column.size, -1).T
        column = np.ascontiguousarray(column).view(f"<U{num_len}")
        for c in range(len(column)):
            cephalopod_numbers[c].append(*column[c])
    cephalopod_numbers = np.array(cephalopod_numbers, dtype=str)
    cephalopod_numbers[cephalopod_numbers == ""] = np.nan
    return cephalopod_numbers


def part1(numbers, operators):
    numbers = np.copy(numbers)
    operators = np.copy(operators)
    if numbers.dtype != int:
        numbers = np.char.strip(numbers)
        numbers = np.where(numbers == "", "nan", numbers)
        numbers = numbers.astype(float)

    amount = numbers.shape[1]
    sub_results = np.zeros(amount)

    # sum
    mask = operators == "+"
    sub_results[mask] = np.nansum(numbers[:, mask], axis=0)

    # prod
    mask = operators == "*"
    sub_results[mask] = np.nanprod(numbers[:, mask], axis=0)

    result = np.sum(sub_results, dtype=int)
    return result


def load_txt(path):
    "load text, split by columns, but keep spaces"
    try:
        with open(path, "r") as file:
            full_text_string = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return np.array([])
    rows = full_text_string.splitlines()

    # operators
    operator_row = rows[-1]

    # calculate max digits in each column (to keep spaces)
    spaces = re.findall(r"(?<=\S)(\s+)(?=\S)", operator_row)
    splitters = []
    for sp in spaces:
        splitters.append(len(sp))

    # operators... only chars
    operator_row = operator_row.replace(" ", "")
    operators = np.array(list(operator_row), dtype=str)

    def split_remove(arr, idx):
        return arr[:idx], arr[idx + 1 :]

    numbers = [[] for _ in range(len(rows) - 1)]
    for idx in splitters:
        for row in range(len(rows) - 1):
            left, rows[row] = split_remove(rows[row], idx)
            numbers[row].append(left)
    for row in range(len(rows) - 1):
        numbers[row].append(rows[row])

    numbers = np.array(numbers, dtype=str)
    return operators, numbers


if __name__ == "__main__":
    operators, numbers = load_txt(PATH)

    print(f"part1: {part1(numbers, operators)}")
    print(f"part2: {part2(numbers, operators)}")
