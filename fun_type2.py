# Return type without argument
# max of two number 
def max(): 
    x=int(input("Enter 1st number:"))
    y=int(input("Enter 2nd number:"))
    if(x>y):
        print("x is max")
        return(x)
    else:
        print("x is max")
        return(y)
    p=max()
    print("max=",p)