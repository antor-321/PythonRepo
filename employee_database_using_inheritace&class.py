# Parent class
class Employee:
    def __init__(self, emp_id, name, address):
        self.emp_id = emp_id
        self.name = name
        self.address = address

    def display_employee(self):
        print("Employee ID :", self.emp_id)
        print("Name        :", self.name)
        print("Address     :", self.address)


# Child class (inherits Employee)
class Salary(Employee):
    def __init__(self, emp_id, name, address, basic_salary):
        super().__init__(emp_id, name, address)
        self.basic_salary = basic_salary

    def calculate_salary(self):
        self.da = self.basic_salary * 0.40
        self.hra = self.basic_salary * 0.25
        self.gross_salary = self.basic_salary + self.da + self.hra

    def display_salary(self):
        self.calculate_salary()
        self.display_employee()
        print("Basic Salary:", self.basic_salary)
        print("DA          :", self.da)
        print("HRA         :", self.hra)
        print("Gross Salary:", self.gross_salary)


# Main Program
emp1 = Salary(101, "SKS", "kakinara", 500000)
emp1.display_salary()
