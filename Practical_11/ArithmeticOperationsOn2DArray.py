import numpy as np
 
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("Array A:")
print(A)

print("\nArray B:")
print(B)
 
print("\nAddition:")
print(A + B)
 
print("\nSubtraction:")
print(A - B)
 
print("\nMultiplication:")
print(A * B)
 
print("\nDivision:")
print(A / B)
 
print("\nTranspose of A:")
print(A.T)
 
print("\nExponential of A:")
print(np.exp(A))