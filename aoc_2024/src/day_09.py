import numpy as np

FILE = "data/day_09.txt"
with open(FILE, "r") as f:
    number = f.read().strip()

digits = np.array([int(digit) for digit in number])


number = 0
idx = 0
if len(digits) % 2 == 0:
    last_num_idx = len(digits) - 2
    last_num = int(last_num_idx / 2)
else:
    last_num_idx = len(digits) - 1
    last_num = int(last_num_idx / 2)

result = np.array([])
running = True
while running:
    if idx % 2 == 0:
        result = np.append(result, number * np.ones(digits[idx]))
        number += 1
    else:

        while digits[idx] > 0:
            if digits[idx] > digits[last_num_idx]:
                result = np.append(result, last_num * np.ones(digits[last_num_idx]))
                digits[idx] -= digits[last_num_idx]
                last_num_idx -= 2
                last_num -= 1
            else:
                result = np.append(result, last_num * np.ones(digits[idx]))
                digits[last_num_idx] -= digits[idx]
                digits[idx] = 0
                if digits[last_num_idx] == 0:
                    last_num_idx -= 2
                    last_num -= 1
    idx += 1
    if last_num_idx - idx < 0:
        running = False


indexes = np.arange(len(result))
checksum = np.sum(indexes * result)
print(checksum)
