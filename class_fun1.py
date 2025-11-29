# No return type without argument in class function\
class A:
    def Add(self):
        x=int(input("Enter a number: "))
        y=int(input("Enter another number: "))
        z=x+y
        print("The sum is:",z)
obj=A()
obj.Add()