import re
import numpy as np

with open("data/day_03.txt", "r") as file:
    text = file.read()
pattern = r"mul\((\d+),(\d+)\)"
matches = re.findall(pattern, text)

summary = 0
if matches:
    for num1, num2 in matches:
        num1, num2 = np.asarray([num1, num2], dtype=float)
        if num1 > 0 and num1 < 1e4 and num2 > 0 and num2 < 1e4:
            summary += num1 * num2
print(summary)
