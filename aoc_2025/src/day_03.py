import numpy as np

PATH = "data/day_03_easy.txt"
PATH = "data/day_03.txt"


def total_joltage(data, digits=12):
    """Solution for both part 1 and part 2
    Universal solution with any amount of digits
    """
    digits = min(digits, data.shape[1])
    rows = np.arange(data.shape[0])
    joltages = np.zeros(data.shape[0], dtype=int)

    for i in range(digits - 1, -1, -1):
        sort_idxs = my_sort(data)
        idxs = np.zeros(data.shape[0], dtype=int)
        highest_idxs = sort_idxs[rows, idxs]

        while not all(highest_idxs <= data.shape[1] - 1 - i):
            increment_mask = ~(highest_idxs <= data.shape[1] - 1 - i)
            idxs[increment_mask] += 1
            highest_idxs = sort_idxs[rows, idxs]

        joltages += data[rows, highest_idxs] * (10**i)

        # modify the row so we can find new second highest digit on the left side of the highest dig
        cols = np.arange(data.shape[1])
        data[rows, :] = np.where(cols <= highest_idxs[rows, None], 0, data[rows, :])
    solution = np.sum(joltages)
    return solution


def my_sort(data):
    idx = np.tile(np.arange(data.shape[1]), (data.shape[0], 1))
    # lexsort: last key has highest priority
    # sort by: (value ascending, index descending)
    sorted_idx = np.lexsort((-idx, data))
    sorted_idx = sorted_idx[:, ::-1]
    return sorted_idx


def part1(data):
    """Part 1 no loops"""
    result = np.argsort(data, axis=1)
    # indices of 2 highest numbers
    sort_idxs = result[:, -2:]
    sort_idxs = sort_idxs[:, ::-1]
    idx_higher = sort_idxs[:, 0]
    idx_lower = sort_idxs[:, 1]
    rows = np.arange(data.shape[0])

    # rows where we can simply take "left digit" and "right digit"
    row_mask = (
        (idx_higher < idx_lower)
        | (idx_higher == data.shape[1] - 1)
        | (data[rows, idx_higher] == data[rows, idx_lower])
    )
    # rows where we have to find new "right digit"
    row_mask = ~row_mask

    # modify the row so we can find new second highest digit on the left side of the highest dig
    cols = np.arange(data.shape[1])
    data[row_mask, :] = np.where(
        cols < idx_higher[row_mask, None], 0, data[row_mask, :]
    )

    # find indices of highest digits
    result[row_mask] = np.argsort(data, axis=1)[row_mask]
    sort_idxs = result[:, -2:]
    # sort it so its "left digit" "right digit"
    digit_idxs = np.sort(sort_idxs, axis=1)
    solution = np.sum(data[rows, digit_idxs[:, 0]] * 10 + data[rows, digit_idxs[:, 1]])

    return solution


if __name__ == "__main__":
    data = np.genfromtxt(PATH, dtype=int, delimiter=1)

    print(f"part1: {total_joltage(np.copy(data), 2)}")
    print(f"part2: {total_joltage(np.copy(data))}")
