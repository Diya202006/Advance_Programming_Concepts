class Person:
    def __init__(self):
        self.name = "Diya"
        self.age = 20

    def show_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Student(Person):
    def __init__(self):
        super().__init__()
        self.roll_no = 101
        self.branch = "Computer Engineering"

    def show_student(self):
        print("Roll No:", self.roll_no)
        print("Branch:", self.branch)
 
obj = Student()

obj.show_person()
obj.show_student()