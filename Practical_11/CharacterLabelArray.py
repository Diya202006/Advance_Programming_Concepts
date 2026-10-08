import numpy as np
 
A = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])
 
columns = ["A", "B"]
 
rows = ["X", "Y", "Z"]

print("     ", columns[0], columns[1])

for i in range(len(A)):
    print(rows[i], A[i])