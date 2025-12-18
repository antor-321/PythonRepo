class Student:
    def __init__(self, name, roll, reg):
        self.name = name
        self.roll = roll
        self.reg = reg

    def show_basic(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Registration No:", self.reg)
class Marks(Student):
    def __init__(self, name, roll, reg, ben, eng, phy, chem, math):
        super().__init__(name, roll, reg)
        self.ben = ben
        self.eng = eng
        self.phy = phy
        self.chem = chem
        self.math = math

    def total_marks(self):
        return self.ben + self.eng + self.phy + self.chem + self.math
class Sports(Marks):
    def __init__(self, name, roll, reg, ben, eng, phy, chem, math, sport):
        super().__init__(name, roll, reg, ben, eng, phy, chem, math)
        self.sport = sport
    def total_marks(self):
        total = super().total_marks()
        if self.sport.lower() != "no":
            total += 4  
        return total

    def division(self):
        total = self.total_marks()
        percent = total / 5

        if percent >= 60:
            return "First Division"
        elif percent >= 45:
            return "Second Division"
        else:
            return "Third Division"

    def display(self):
        self.show_basic()
        print("Sports:", self.sport)
        print("Total Marks:", self.total_marks())
        print("Division:", self.division())
name = input("Enter name: ")
roll = int(input("Enter roll number: "))
reg = input("Enter registration number: ")

ben = int(input("Bengali marks: "))
eng = int(input("English marks: "))
phy = int(input("Physics marks: "))
chem = int(input("Chemistry marks: "))
math = int(input("Math marks: "))

sport = input("Plays sports? (Yes/No): ")