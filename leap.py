# WAP to check the year is leap year or not 
y=int(input("Enter a year")) 
if((y%100==0)and(y%400==0)):
  print("Leap year")
elif ((y%100!=0))and(y%4==0)):
  print("Leap year")
else:
  print("None leap year") 
