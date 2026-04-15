class A:
    def methodA(self):
        print("A")

class B(A):
    def methodB(self):
        print("B")

class C(A):
    def methodC(self):
        print("C")

class D(B, C):
    def methodD(self):
        print("D")

obj = D()
obj.methodA()
obj.methodB()
obj.methodC()
obj.methodD()
# In this example, we have four classes: A, B, C, and D. The class D inherits from both B and C, which in turn
#  inherit from A. This is an example of hybrid inheritance, where a class can inherit
# from multiple classes that may have a common ancestor. The class D can access methods from both B and C, 
# as well as the method from A. When we create an instance of the D class and call the methods, it successfully 
# accesses the methodA() from class A, methodB() from class B, methodC() from class C, and its own methodD(). 
# This demonstrates how hybrid inheritance allows a class to inherit attributes and behaviors from multiple classes,
#  providing flexibility in code organization and reuse.
