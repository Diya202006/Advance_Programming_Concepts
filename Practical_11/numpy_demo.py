import numpy as np
 
arr = np.array([10, 20, 30, 40, 50])

print("Array:", arr)
 
print("First element:", arr[0])
print("Third element:", arr[2])
 
print("Addition:", arr + 5)
print("Subtraction:", arr - 5)
print("Multiplication:", arr * 2)
print("Division:", arr / 2)
 
print("Sum:", np.sum(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Mean:", np.mean(arr))
 
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n2D Array:")
print(matrix)

print("Shape:", matrix.shape)
print("Number of dimensions:", matrix.ndim)