# Implement the code 10 functions of Dictionary

student = {
    "name": "Diya",
    "age": 20,
    "branch": "CSE",
    "marks": 90
}

print("Original Dictionary:", student)
 
print("1. Name using get():", student.get("name"))
 
print("2. Keys:", student.keys())
 
print("3. Values:", student.values())
 
print("4. Items:", student.items())
 
student.update({"marks": 95})
print("5. After update():", student)
 
age = student.pop("age")
print("6. Removed age:", age)
print("   Dictionary:", student)
 
item = student.popitem()
print("7. Removed last item:", item)
print("   Dictionary:", student)
 
student.setdefault("city", "Kolhapur")
print("8. After setdefault():", student)
 
student_copy = student.copy()
print("9. Copied Dictionary:", student_copy)
 
temp = {"A": 1, "B": 2}
temp.clear()
print("10. After clear():", temp)
