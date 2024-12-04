import re
import numpy as np

with open("data/day_03.txt", "r") as file:
    text = file.read()
pattern_mul = r"mul\((\d+),(\d+)\)"
pattern_enable = r"do()"
pattern_disable = r"don't()"
patterns = [pattern_mul, pattern_mul, pattern_disable]

matches = []

for pattern in [pattern_enable, pattern_mul, pattern_disable]:
    for match in re.finditer(pattern, text):
        if pattern == pattern_mul:
            matches.append((pattern, match.start(), match.group(1), match.group(2)))
        else:
            matches.append((pattern, match.start()))

matches.sort(key=lambda x: x[1])

summary = 0
enable = True
if matches:
    for match in matches:
        if match[0] == pattern_enable:
            enable = True
        elif match[0] == pattern_disable:
            enable = False
        else:
            if enable:
                num1, num2 = match[2], match[3]
                num1, num2 = np.asarray([num1, num2], dtype=float)
                if num1 > 0 and num1 < 1e4 and num2 > 0 and num2 < 1e4:
                    summary += num1 * num2
print(summary)
