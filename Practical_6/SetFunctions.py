# Implement the code 10 functions of set
 
set1 = {10, 20, 30, 40, 50}
set2 = {40, 50, 60, 70, 80}

print("Original Set 1:", set1)
print("Original Set 2:", set2)
 
set1.add(90)
print("1. After add():", set1)
 
set1.remove(90)
print("2. After remove():", set1)
 
set1.discard(50)
print("3. After discard():", set1)
 
removed = set1.pop()
print("4. Element removed using pop():", removed)
print("   Set after pop():", set1)
 
set1 = {10, 20, 30, 40, 50}
 
temp = {1, 2, 3}
temp.clear()
print("5. After clear():", temp)
 
print("6. Union:", set1.union(set2))
 
print("7. Intersection:", set1.intersection(set2))
 
print("8. Difference:", set1.difference(set2))
 
set3 = {10, 20}
print("9. Is set3 subset of set1?:", set3.issubset(set1))
 
print("10. Is set1 superset of set3?:", set1.issuperset(set3))