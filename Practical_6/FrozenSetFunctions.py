# Implement the code 10 functions of Frozen set

fs1 = frozenset([10, 20, 30, 40, 50])
fs2 = frozenset([40, 50, 60, 70, 80])

print("Frozen Set 1:", fs1)
print("Frozen Set 2:", fs2)
 
print("1. Union:", fs1.union(fs2))
 
print("2. Intersection:", fs1.intersection(fs2))
 
print("3. Difference:", fs1.difference(fs2))
 
print("4. Symmetric Difference:",
      fs1.symmetric_difference(fs2))
 
fs3 = frozenset([10, 20])
print("5. Is fs3 subset of fs1?:",
      fs3.issubset(fs1))
 
print("6. Is fs1 superset of fs3?:",
      fs1.issuperset(fs3))
 
fs4 = frozenset([100, 200])
print("7. Are fs1 and fs4 disjoint?:",
      fs1.isdisjoint(fs4))
 
print("8. Length of fs1:", len(fs1))
 
print("9. Minimum value:", min(fs1))
 
print("10. Maximum value:", max(fs1))