class Company:
    def __init__(self):
        self._company_name = "TCS"        
        self._location = "Mumbai"        
    def show_company(self):
        print("Company Name:", self._company_name)
        print("Location:", self._location)


class Employee:
    def __init__(self):
        self.__employee_name = "Rahul"    
        self.__salary = 50000            

    def show_employee(self):
        print("Employee Name:", self.__employee_name)
        print("Salary:", self.__salary)

class Manager(Company, Employee):
    def __init__(self):
        Company.__init__(self)
        Employee.__init__(self)

    def show_manager(self):
        print("Manager Details:")
        print("Company Name:", self._company_name)   
        print("Location:", self._location)           
 
        self.show_employee()
 
obj = Manager()

obj.show_company()
obj.show_manager()