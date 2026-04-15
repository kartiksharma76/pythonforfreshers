class Parent:
    def property(self):
        print("Property")
    
class Child1(Parent):
  def property(self):
     print("Property of Child1")

class Child2(Parent):
    def property(self):
        print("Property of Child2")

child1 = Child1()
child2 = Child2()
child1.property()  # Output: Property of Child1
child2.property()  # Output: Property of Child2
# In this example, we have a Parent class with a method called property(). 
# The Child1 and Child2 classes both inherit from the Parent class and override the property()
#  method to provide their own implementation. When we create instances of Child1 and Child2 a
# nd call the property() method, it executes the overridden method in each child class, demonstrating
#  hierarchical inheritance. Each child class can have its own unique implementation of the inherited 
# method while still maintaining the relationship with the parent class.
