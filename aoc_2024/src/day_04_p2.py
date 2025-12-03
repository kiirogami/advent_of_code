import numpy as np


def check_text(pos, dir):
    text_located = ""
    dir = np.asarray(dir)
    for i in range(-1, 2):
        text_located += lines[(pos + i * dir[0])[0]][(pos + i * dir[1])[1]]
    if text_located == text or "".join(reversed(text_located)) == text:
        return True
    return False


def check_letter(pos):
    pos = np.asarray(pos)
    if lines[pos[0]][pos[1]] == "A":
        if (check_text(pos, [1, 1]) and check_text(pos, [1, -1])):
            return 1
    return 0


with open("data/day_04.txt", "r") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
lines = np.asarray(lines)
text = "MAS"
text_len = len(text)
y_len = len(lines)
x_len = len(lines[0])
amount = 0
for y in range(1, y_len - 1):
    for x in range(1, x_len - 1):
        amount += check_letter([y, x])
print(amount)
