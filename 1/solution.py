import numpy as np

data = np.loadtxt("input.txt")
distance = np.sum(np.abs(np.sort(data[:, 0]) - np.sort(data[:, 1])))
print(distance)
