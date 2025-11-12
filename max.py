# WAP to max of 3 number 
x=int(input("Enter 1st number:")) 
y=int(input("Enter 2nd number:"))
z=int(input("Enetr 3rd number:")) 
if ((x>y)and(x>z)):
  print("x=",x,"is max") 
elif ((y>x)and(y>z)):
  print("y=",y,"y is max")
else:
  print("z=",z,"is max")
  
