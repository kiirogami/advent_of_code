import numpy as np

PATH = "data/day_02_easy.txt"
PATH = "data/day_02.txt"
DIVS = {}


def part1(data):
    solution = 0
    for id_range in data:
        lower, upper = np.str_.split(id_range, "-")
        lower, upper = int(lower), int(upper)
        for id in range(lower, upper + 1):
            s_id = str(id)
            str_len = len(s_id)
            if str_len % 2 == 0:
                left, right = s_id[str_len // 2 :], s_id[: str_len // 2]
                if left == right:
                    solution += id
            else:
                continue
    return solution


def part2(data):
    """kinda ugly bruteforce, idk if there is smarter solution"""
    solution = 0
    for id_range in data:
        lower, upper = np.str_.split(id_range, "-")
        lower, upper = int(lower), int(upper)
        for id in range(lower, upper + 1):
            s_id = np.array(list(str(id)), dtype=int)
            digits = len(s_id)
            divs = divisors(digits)
            divs = divs[divs != digits]
            for div in divs:
                temp_id = s_id.reshape(-1, div)  # separate id digits to check pattern
                if np.all(temp_id == temp_id[0, :], axis=1).all():
                    solution += id
                    break
    return solution


def divisors(n):
    if n not in DIVS:
        arr = np.arange(1, int(np.sqrt(n)) + 1)
        divs = arr[n % arr == 0]
        all_divs = np.unique(np.concatenate((divs, n // divs)))
        DIVS[n] = all_divs
    return DIVS[n]


def load_txt(path):
    try:
        with open(path, "r") as file:
            full_text_string = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{path}' was not found.")
        return np.array([])
    rows = full_text_string.splitlines()
    data = []
    for row in rows:
        ranges = row.split(",")
        for range in ranges:
            if range != "":
                data.append(range)
    data = np.asarray(data, dtype=str)
    return data


if __name__ == "__main__":
    data = load_txt(PATH)
    divisors(100)
    if data.shape != (0,):
        # print(f"part1: {part1(data)}")
        print(f"part2: {part2(data)}")
