# Multivalue argument in python 
def Add(s,*a):
    for i in a:
        p=s+i
        s=p
    return(p)
x= Add(1,2)
print(x)