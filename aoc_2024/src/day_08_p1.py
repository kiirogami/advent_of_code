import numpy as np

FILE_PATH = "data/day_08.txt"


def main():
    antenas = {}
    map = []
    with open(FILE_PATH, "r") as file:
        y = 0
        for line in file:
            row = line.strip()
            for x in range(len(row)):
                if row[x] != ".":
                    if row[x] not in antenas:
                        antenas[row[x]] = [[y, x]]
                    else:
                        antenas[row[x]].append([y, x])
            map.append(list(row))
            y += 1
    print(map_antinodes(map, antenas))


def map_antinodes(map, antenas):
    amount = 0
    for key in antenas:
        B = set(
            (i, j)
            for i in range(len(antenas[key]))
            for j in range(i + 1, len(antenas[key]))
        )
        while B:
            i, j = B.pop()
            pos_i, pos_j = np.array(antenas[key][i]), np.array(antenas[key][j])
            vec = pos_j - pos_i
            new_pos = pos_j + vec
            amount += create_antinode(map, new_pos)
            new_pos = pos_i - vec
            amount += create_antinode(map, new_pos)
    return amount


def create_antinode(map, position):
    limits = np.array([len(map), len(map[0])])
    if all(position < limits) and all(position >= 0):
        y, x = position
        if map[y][x] != "#":
            map[y][x] = "#"
            return 1
    return 0


if __name__ == "__main__":
    main()
