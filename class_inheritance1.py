class A:
    def funA(self):
        self.x=10
        print("class A funA x= ", self.x)
class B:
    def funB(self):
        self.y=20
        print("class B funB y= ", self.y)
class C(A,B):
    def funC(self):
        self.z=30
        print("class C funC z= ", self.z)
obj=C()
obj.funC()
obj.funB()
obj.funA()