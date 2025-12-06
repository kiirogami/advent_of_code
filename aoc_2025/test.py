import numpy as np

arr = np.array(["10", "", "  20", ""])
arr = np.char.strip(arr)
arr = np.where(arr == "", "nan", arr)
arr = arr.astype(float)

print(arr)
