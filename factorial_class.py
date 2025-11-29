# Factorial program using class and object
class A: 
    def fact(self): 
        n=int(input("Enter a number to find its factorial: "))
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        print("The factorial of",n,"is:",fact)
obj=A()
obj.fact()
