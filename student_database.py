class employee:
    def input(self, Id, Name, Address, Basic_salary):
        self.Id = Id
        self.Name = Name
        self.Address = Address
        self.Basic_salary = Basic_salary

    def calculation(self):
        self.Da = self.Basic_salary * 0.40
        self.Hra = self.Basic_salary * 0.25
        self.Gross = self.Basic_salary + self.Da + self.Hra

    def output(self):
        print("Name:", self.Name)
        print("Id:", self.Id)
        print("Address:", self.Address)
        print("Basic salary:", self.Basic_salary)
        print("Gross Salary:", self.Gross)

        # Tax Slab
        if self.Gross < 1:
            print("0% Tax")
        elif self.Gross >= 1.30 and self.Gross < 2.30:
            print("10% Tax")
        elif self.Gross >= 2.30:
            print("20% Tax")


# ---------- Main Program ---------- #

Id = input("Enter Id: ")
Name = input("Enter Name: ")
Address = input("Enter Address: ")

Basic_salary = float(input("Enter Basic Salary: "))

obj = employee()
obj.input(Id, Name, Address, Basic_salary)
obj.calculation()
obj.output()
