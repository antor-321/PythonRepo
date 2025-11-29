# Return without Argument in class function
class A: 
    def Add(self): 
        x=int(input("Enter a number: "))
        y=int(input("Enter another number: "))
        z=x+y
        return z
obj=A()
p=obj.Add()
print("The return value is:",p)