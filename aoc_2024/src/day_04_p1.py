import numpy as np


def check_direction(pos, dir):
    dir = np.asarray(dir)
    pos = np.asarray(pos)
    limit = (text_len - 1) * dir + pos
    limit_low = np.array([0, 0])
    limit_up = np.array([y_len, x_len])
    if all(limit < limit_up) and all(limit >= limit_low):
        text_located = ""
        for i in range(text_len):
            text_located += lines[(pos + i * dir)[0]][(pos + i * dir)[1]]
        return 1 if text_located == text else 0
    else:
        return 0


def check_all_directions(pos):
    # so ugly but w/e
    directions = [
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
        [1, 1],
        [-1, -1],
        [-1, 1],
        [1, -1],
    ]
    amount = 0
    if lines[pos[0]][pos[1]] == "X":
        for dir in directions:
            amount += check_direction(pos, dir)
    return amount


with open("data/day_04.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
text = "XMAS"
text_len = len(text)
y_len = len(lines)
x_len = len(lines[0])
amount = 0
for y in range(y_len):
    for x in range(x_len):
        amount += check_all_directions([y, x])
print(amount)
