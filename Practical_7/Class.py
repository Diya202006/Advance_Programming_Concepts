class Student:
    name = ""
    age = 0
    branch = ""
 
    def __init__(self, name, age, branch):
        self.name = name
        self.age = age
        self.branch = branch
 
    def display(self):
        print("Student Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)
 
student1 = Student("Diya", 20, "Computer Science")
 
student1.display()