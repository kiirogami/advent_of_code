import numpy as np

numbers = np.array([1, 4, 12, 17, 30])

ranges = np.array([[3, 5], [10, 14], [16, 20]])

num_in_range = np.any(
    (numbers[:, None] >= ranges[:, 0]) & (numbers[:, None] <= ranges[:, 1]), axis=1
)

print(num_in_range)
