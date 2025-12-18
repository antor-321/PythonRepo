class A:
    def fun(self):
        self.x=10
        print("class A funA x= ", self.x)
class B:
    def fun(self):
        self.y=20
        print("class B funB y= ", self.y)
class C(B,A):
    def fun(self):
        super().fun()
        self.z=30
        print("class C funC z= ", self.z)
obj=C()
obj.fun()
obj.fun()
obj.fun()