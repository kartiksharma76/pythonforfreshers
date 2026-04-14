# ================= INPUT / OUTPUT IN PYTHON =================

# Input and Output are used to interact with the user.
# Input → takes data from user
# Output → displays data to user


# ---------------------------------------------------------------------------
# 1. Output (print function):
# Used to display data on the screen.

# Syntax:
# print(value)

# Example:
# print("Hello World")

# Multiple values:
# print("Name:", "Kartik")

# Using variables:
# name = "Kartik"
# print(name)


# ---------------------------------------------------------------------------
# 2. Input (input function):
# Used to take input from user.

# Syntax:
# variable = input("message")

# Example:
# name = input("Enter your name: ")

# Note:
# input() always takes data as STRING by default.


# ---------------------------------------------------------------------------
# 3. Taking Different Data Types as Input:

# (a) Integer input:
# age = int(input("Enter age: "))

# (b) Float input:
# price = float(input("Enter price: "))

# (c) String input:
# name = input("Enter name: ")


# ---------------------------------------------------------------------------
# 4. Type Conversion (important with input):

# Since input() gives string, we convert it:

# Example:
# a = input("Enter number: ")
# b = int(a)   # convert string to integer

# Short way:
# num = int(input("Enter number: "))


# ---------------------------------------------------------------------------
# 5. Output Formatting:

# (a) Using comma:
# print("Age is", 21)

# (b) Using f-string (modern and best way):
# name = "Kartik"
# print(f"My name is {name}")

# (c) Using format():
# print("My name is {}".format(name))


# ---------------------------------------------------------------------------
# 6. Escape Characters:
# Used to format output text.

# \n → New line
# \t → Tab space
# \" → Double quote inside string

# Example:
# print("Hello\nWorld")


# ---------------------------------------------------------------------------
# 7. end parameter in print():
# Used to change default newline behavior.

# Example:
# print("Hello", end=" ")
# print("World")
# Output: Hello World


# ---------------------------------------------------------------------------
# ================= IMPORTANT SUMMARY =================

# print() → output show karta hai
# input() → user se data leta hai
# input always string deta hai
# int(), float() → type conversion ke liye use hota hai
# f-string → best formatting method
class InputOutputDemo:

    def __init__(self):
        print("=== Input / Output Demo ===")

    def basic_output(self):
        # Output using print()
        print("\n--- Basic Output ---")
        print("Hello World")
        print("My name is Kartik")

    def basic_input(self):
        # Taking input (string)
        print("\n--- Basic Input ---")
        name = input("Enter your name: ")
        print("Hello", name)

    def type_conversion(self):
        # Taking numeric input using type conversion
        print("\n--- Type Conversion ---")
        age = int(input("Enter your age: "))
        price = float(input("Enter price: "))

        print("Age:", age)
        print("Price:", price)

    def formatting_output(self):
        # Output formatting methods
        print("\n--- Output Formatting ---")
        name = "Kartik"
        age = 21

        print("Name is", name, "and age is", age)   # using comma
        print(f"Name is {name} and age is {age}")   # f-string
        print("Name is {} and age is {}".format(name, age))  # format()

    def escape_characters(self):
        # Escape characters
        print("\n--- Escape Characters ---")
        print("Hello\nWorld")   # new line
        print("Hello\tWorld")   # tab space
        print("He said \"Hello\"")

    def end_parameter(self):
        # Using end parameter
        print("\n--- End Parameter ---")
        print("Hello", end=" ")
        print("World")


# Run all methods
obj = InputOutputDemo()
obj.basic_output()
obj.basic_input()
obj.type_conversion()
obj.formatting_output()
obj.escape_characters()
obj.end_parameter()