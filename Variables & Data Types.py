# ================= VARIABLES & DATA TYPES (FULL COMMENT NOTES) =================

# 1. Variable:
# A variable is a container used to store data in memory.
# Example:
# name = "Kartik"
# 'name' is variable and "Kartik" is the value stored inside it.


# 2. Data Types:
# Data types define the type of value a variable holds.


# (a) String (str):
# Used to store text data.
# Always written inside single (' ') or double (" ") quotes.
# Example:
# text = "Hello"


# (b) Integer (int):
# Used to store whole numbers (positive or negative, without decimal).
# Example:
# num = 10


# (c) Float (float):
# Used to store decimal (floating point) numbers.
# Example:
# pi = 3.14


# (d) Boolean (bool):
# Used to store logical values: True or False.
# Example:
# is_valid = True


# (e) List (list):
# Ordered collection of elements.
# Mutable → values can be changed after creation.
# Allows duplicate values.
# Example:
# my_list = [1, 2, 3]


# (f) Tuple (tuple):
# Ordered collection of elements.
# Immutable → values cannot be changed after creation.
# Allows duplicate values.
# Example:
# my_tuple = (1, 2, 3)


# (g) Set (set):
# Unordered collection of unique elements.
# Does not allow duplicate values.
# Example:
# my_set = {1, 2, 3}


# (h) Dictionary (dict):
# Collection of key-value pairs.
# Each key maps to a value.
# Example:
# my_dict = {"name": "Kartik"}


# ================= IMPORTANT CONCEPTS =================


# Dynamic Typing:
# Python automatically detects the data type of a variable.
# Example:
# x = 10        → integer
# x = "Hello"   → now string (same variable, different type)


# Type Checking:
# Used to check the data type of a variable using type() function.
# Example:
# print(type(x))


# Type Conversion:
# Used to convert one data type into another.
# Example:
# a = "10"
# b = int(a)   → converts string to integerF

class PythonBasics:
    def __init__(self):
        print("===Variables & data types Demo ===")

    def variables_demo(self):
        # Variables are used to store data in Python. They can hold different types of data, such as numbers, strings, lists, etc.
        # Here are some examples of variables in Python:
        # Variables(Store values)
        name = "Kartik"     # string
        age = 21            # integer
        height = 5.9        # float
        is_student = True   # boolean

        print("Name:",name)
        print("Age:",age)
        print("Height:",height)
        print("Is Student:",is_student)

    def data_types_demo(self):
        # Different data types in Python include:
        # 1. String: A sequence of characters enclosed in quotes.
        # 2. Integer: A whole number without a decimal point.
        # 3. Float: A number with a decimal point.
        # 4. Boolean: A data type that can only be True or False.
        # Here are some examples of data types in Python:

        # String
        text = "Hello python"
        print("\nString:", text, "| Type:", type(text))

        # Integer
        number = 42
        print("Integer:", number, "| Type:", type(number))
    
        # Float
        pi = 3.14
        print("Float:", pi, "| Type:", type(pi))

        # Boolean
        flag = False
        print("Boolean:", flag, "| Type:", type(flag))
     
        # 5. List (mutable)
        my_list = [1, 2, 3, 4]
        print("List:", my_list, "| Type:", type(my_list))

        # 6. Tuple (immutable)
        my_tuple = (10, 20, 30)
        print("Tuple:", my_tuple, "| Type:", type(my_tuple))

        # 7. Set (unique values)
        my_set = {1, 2, 3, 3}
        print("Set:", my_set, "| Type:", type(my_set))
        
        # 8. Dictionary (key-value pair)
        my_dict = {"name": "Kartik", "age": 21}
        print("Dictionary:", my_dict, "| Type:", type(my_dict))

obj = PythonBasics()
obj.variables_demo()
obj.data_types_demo()


