import numpy as np

PATH = "data/day_05_easy.txt"
PATH = "data/day_05.txt"


def part2(ranges):
    """How many ingredient IDs are considered to be fresh according to the fresh ingredient ID ranges"""
    ranges = merge_ranges(ranges)
    amounts = ranges[:, 1] - ranges[:, 0] + 1
    amount = np.sum(amounts)
    return amount


def part1(ranges, ingredients):
    """find the amount of fresh ingredients in list of available ingredients"""
    ranges = merge_ranges(ranges)

    fresh_mask = np.any(
        (ingredients[:, None] >= ranges[:, 0]) & (ingredients[:, None] <= ranges[:, 1]),
        axis=1,
    )
    fresh_amount = np.sum(fresh_mask)
    return fresh_amount


def merge_ranges(ranges):
    ranges = list(map(tuple, ranges))
    ranges = sorted(ranges)

    merged = []
    cur_start, cur_end = ranges[0]

    for s, e in ranges[1:]:
        if s <= cur_end + 1:
            cur_end = max(cur_end, e)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = s, e
    merged.append((cur_start, cur_end))

    return np.array(merged)


def load_txt(path):
    try:
        with open(path, "r") as file:
            full_text_string = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return np.array([])
    rows = full_text_string.splitlines()
    ingredients = []
    fresh_ranges = []
    for row in rows:
        if "-" in row:
            ranges = row.split("-")
            lower = ranges[0]
            upper = ranges[1]
            fresh_ranges.append((lower, upper))
        elif row == "":
            continue
        else:
            ingredients.append(row)
    fresh_ranges = np.asarray(fresh_ranges, dtype=int)
    ingredients = np.asarray(ingredients, dtype=int)
    return fresh_ranges, ingredients


if __name__ == "__main__":
    ranges, ingredients = load_txt(PATH)
    pass
    print(f"part1: {part1(np.copy(ranges), np.copy(ingredients))}")
    print(f"part2: {part2(np.copy(ranges))}")
