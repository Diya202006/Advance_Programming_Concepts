# Attendance System

attendance = {}

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
 
for day in days:
    students = input(f"Enter students present on {day} (separated by spaces): ").split()
    attendance[day] = set(students)
 
all_students = attendance[days[0]]
for day in days[1:]:
    all_students = all_students.intersection(attendance[day])
 
unique_students = set()
for day in days:
    unique_students = unique_students.union(attendance[day])
 
attendance_count = {}

for day in days:
    for student in attendance[day]:
        if student in attendance_count:
            attendance_count[student] += 1
        else:
            attendance_count[student] = 1

one_day_students = set()

for student, count in attendance_count.items():
    if count == 1:
        one_day_students.add(student)
 
print("\n--- Attendance Report ---")
print("Students who attended all classes:", all_students)
print("Students who attended only one class:", one_day_students)
print("Total unique students:", len(unique_students))
print("All unique students:", unique_students)