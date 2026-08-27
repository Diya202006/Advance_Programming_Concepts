# Implement the code 10 functions of Tuple
 
numbers = (10, 20, 30, 20, 40, 50)

print("Original Tuple:", numbers)
 
print("1. Count of 20:", numbers.count(20))
 
print("2. Index of 30:", numbers.index(30))
 
print("3. Length:", len(numbers))
 
print("4. Maximum value:", max(numbers))
 
print("5. Minimum value:", min(numbers))
 
print("6. Sum:", sum(numbers))
 
print("7. Sorted Tuple:", sorted(numbers))
 
list1 = [100, 200, 300]
new_tuple = tuple(list1)
print("8. List converted to Tuple:", new_tuple)
 
tuple1 = (0, 0, 10, 0)
print("9. Any non-zero value?:", any(tuple1))
 
tuple2 = (10, 20, 30, 40)
print("10. Are all values non-zero?:", all(tuple2))