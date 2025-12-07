import numpy as np

PATH = "data/day_07_easy.txt"
PATH = "data/day_07.txt"


def main():
    data = np.genfromtxt(PATH, dtype=str, delimiter=1)
    data, p1_result = part1(data)
    p2_result = part2(data)
    print(f"part1: {p1_result}")
    print(f"part2: {p2_result}")


def part1(data):
    # beam flow
    data = data.astype("<U2")
    data[data == "S"] = "1"
    data[data == "."] = "0"
    data[data == "^"] = "-1"
    data = data.astype(int)

    rows, cols = data.shape
    splitters_used = 0
    for r in range(1, rows):
        for c in range(cols):
            beam_above = data[r - 1][c]
            if beam_above > 0:
                # if splitter
                if c > 0 and c < cols - 1 and data[r, c] < 0:
                    data[r, c - 1] += beam_above
                    data[r, c + 1] += beam_above
                    splitters_used += 1
                else:
                    data[r, c] += beam_above

    return data, splitters_used


def part2(data):
    result = np.sum(data[-1], dtype=int)
    return result


if __name__ == "__main__":
    main()
