class Grandparent:
    def house(self):
        print("House")

class Parent(Grandparent):
    def car(self):
        print("Car")

class Child(Parent):
    def bike(self):
        print("Bike")


child = Child()
child.house()  # Output: House
child.car()    # Output: Car
child.bike()   # Output: Bike
# In this example, we have three classes: Grandparent, Parent, and Child. The Child class inherits from the Parent class, which in turn inherits from the Grandparent class. This is an example of multilevel inheritance. The Child class can access methods from both the Parent and Grandparent classes. When we create an instance of the Child class and call the methods, it successfully accesses the house() method from the Grandparent class, the car() method from the Parent class, and its own bike() method. 
# Multilevel inheritance allows for a hierarchical relationship between classes, where a child class can inherit
# attributes and behaviors from multiple levels of parent classes. This promotes code reusability and helps in creating a more organized class structure.
# In this example, the Child class can access the house() method from the Grandparent class, the car() method from the Parent class, and its own bike() method. This demonstrates how multilevel inheritance allows a child class to inherit attributes and behaviors from multiple levels of parent classes.
# Multilevel inheritance promotes code reusability and helps in creating a more organized class structure. It allows for a hierarchical relationship between classes, where a child class can inherit attributes and behaviors from multiple levels of parent classes.