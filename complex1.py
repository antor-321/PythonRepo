class complex:
    def input(self,r,i):
        self.real=r
        self.img=i
    def add(self,p,q):
        t=complex()
        t.real=p.real+q.real
        t.img=p.img+q.img
        return(t)
    def output(self):
        if self.img<0:
            print(f"{self.real}{self.img}i")
        else:
             print(f"{self.real}+{self.img}i")
x1=int(input("Enter real no:"))   
y1=int(input("Enter img no:"))
x2=int(input("Enter real no:"))
y2=int(input("Enter img no:"))
D=complex()
A=complex()
B=complex()
C=complex()
A.input(x1,y1)
B.input(x2,y2)
D=C.add(A,B)
print("1st object:")
A.output()
print("2nd object:")
B.output()
print("sum=")
D.output()