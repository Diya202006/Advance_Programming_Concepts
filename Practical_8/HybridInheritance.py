class Student:
    def student_details(self):
        print("Student Name: Diya")
        print("Roll No: 101")

class Engineering(Student):
    def engineering_details(self):
        print("Branch: Computer Engineering")

class Management(Student):
    def management_details(self):
        print("Course: Business Management")

class CollegeStudent(Engineering, Management):
    def college_details(self):
        print("College: D. Y. Patil College")
 
obj = CollegeStudent()

obj.student_details()
obj.engineering_details()
obj.management_details()
obj.college_details()