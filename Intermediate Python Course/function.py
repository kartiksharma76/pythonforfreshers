# 🔹 1. Introduction

# A function in Python is a reusable block of code designed to perform a specific task.
# Functions improve:

# Code reusability
# Modularity
# Readability
# Maintainability

# When organized inside a class, functions are called methods and follow Object-Oriented Programming (OOP) principles.

# class → Blueprint for object creation
# def → Defines a function
# self → Reference to current object
# parameters → Input values
# return → Output value

# 🔹 2. Defining a Function
from os import name


class FunctionDemo:
    # No arguments, no return value
    def greet(self):
        print("hello Kartik")


    # 2. With arguments, no return value
    def greet(self, name):
        print("hello", name)

    # 3. With arguments, with return value
    def add(self, a, b):
        return a+ b
    
    # 4. No arguments, with return value
    def get_number(self):
        return 10
    # 5. Default parameters
    def greet_default(self, name="Guest"):
        print("hello", name)

    # 6. keyword arguments
    def student(self, name, age):
        print("Name:", name)
        print("Age:", age)

    # 7. Lambda function (inside a method)
    def get_square(self, x):
        square = lambda a: a ** 2
        return square(x)
    
# ================= MAIN EXECUTION =================
obj = FunctionDemo() 

# Calling methods
obj.greet("Kartik")  # Output: hello Kartik
print(obj.add(5, 3))  # Output: 8
print(obj.get_number())  # Output: 10
obj.greet_default()  # Output: hello Guest
obj.greet_default("aman")  # Output: hello Alice
obj.student(age=20, name="naman")  # Output: Name: Bob, Age: 20
print(obj.get_square(4))  # Output: 16
