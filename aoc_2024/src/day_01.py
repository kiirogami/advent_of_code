import numpy as np

data = np.loadtxt("data/day_01.txt")
col1 = np.sort(data[:, 0])
col2 = np.sort(data[:, 1])
distance = np.sum(np.abs(col1 - col2))
print(distance)

# part 2
count_list = np.array([np.count_nonzero(col2 == val) for val in col1])
sim_score = np.sum(col1 * count_list)
print(sim_score)
