# ================= PYTHON OPERATORS (FULL THEORY IN COMMENTS) =================

# Operators are symbols used to perform operations on variables and values.

# ---------------------------------------------------------------------------
# 1. Arithmetic Operators:
# Used to perform mathematical calculations.

# +  → Addition (adds two values)
# -  → Subtraction (subtracts second value from first)
# *  → Multiplication (multiplies values)
# /  → Division (returns float result)
# %  → Modulus (returns remainder)
# ** → Exponentiation (power)
# // → Floor Division (returns integer result)


# ---------------------------------------------------------------------------
# 2. Comparison Operators:
# Used to compare two values and return True or False.

# == → Equal to
# != → Not equal to
# >  → Greater than
# <  → Less than
# >= → Greater than or equal to
# <= → Less than or equal to


# ---------------------------------------------------------------------------
# 3. Logical Operators:
# Used to combine multiple conditions.

# and → True if both conditions are True
# or  → True if at least one condition is True
# not → Reverses the result (True → False, False → True)


# ---------------------------------------------------------------------------
# 4. Assignment Operators:
# Used to assign and update values in variables.

# =   → Assign value
# +=  → Add and assign (a = a + value)
# -=  → Subtract and assign
# *=  → Multiply and assign
# /=  → Divide and assign
# %=  → Modulus and assign
# **= → Power and assign
# //= → Floor divide and assign


# ---------------------------------------------------------------------------
# 5. Identity Operators:
# Used to compare memory locations (object identity).

# is     → True if both variables refer to same object
# is not → True if variables refer to different objects

# Note:
# "==" compares values
# "is" compares memory location


# ---------------------------------------------------------------------------
# 6. Membership Operators:
# Used to check if a value exists in a sequence (list, tuple, etc.)

# in     → True if value exists
# not in → True if value does not exist


# ---------------------------------------------------------------------------
# 7. Bitwise Operators:
# Used to perform operations at binary (bit) level.

# &  → AND (both bits must be 1)
# |  → OR (at least one bit is 1)
# ^  → XOR (bits must be different)
# ~  → NOT (inverts bits)
# << → Left Shift (shifts bits left)
# >> → Right Shift (shifts bits right)


# ---------------------------------------------------------------------------
# 8. Ternary Operator:
# Used as a shortcut for if-else in one line.

# Syntax:
# value_if_true if condition else value_if_false

# Example:
# status = "Adult" if age >= 18 else "Minor"


# ---------------------------------------------------------------------------
# 9. Walrus Operator (:=):
# Used to assign value inside an expression.

# Helps reduce lines of code.

# Example:
# if (n := len("Hello")) > 5:
#     print("Greater")
# else:
#     print("Smaller or equal")


# ---------------------------------------------------------------------------
# ================= IMPORTANT SUMMARY =================

# Arithmetic → Calculations
# Comparison → True/False check
# Logical → Combine conditions
# Assignment → Update values
# Identity → Same object check
# Membership → Value exists or not
# Bitwise → Binary operations
# Ternary → Short if-else
# Walrus → Assign inside condition


class OperatorsDemo:

    def __init__(self):
        print("=== Python Operators Demo ===\n")

    # 1. Arithmetic Operators
    def arithmetic_operators(self):
        print("=== Arithmetic Operators ===")
        a = 10
        b = 3
        print("a + b =", a + b)
        print("a - b =", a - b)
        print("a * b =", a * b)
        print("a / b =", a / b)
        print("a % b =", a % b)
        print("a ** b =", a ** b)
        print("a // b =", a // b)
        print()

    # 2. Comparison Operators
    def comparison_operators(self):
        print("=== Comparison Operators ===")
        a = 10
        b = 3
        print("a == b:", a == b)
        print("a != b:", a != b)
        print("a > b:", a > b)
        print("a < b:", a < b)
        print("a >= b:", a >= b)
        print("a <= b:", a <= b)
        print()

    # 3. Logical Operators
    def logical_operators(self):
        print("=== Logical Operators ===")
        x = True
        y = False
        print("x and y:", x and y)
        print("x or y:", x or y)
        print("not x:", not x)
        print()

    # 4. Assignment Operators
    def assignment_operators(self):
        print("=== Assignment Operators ===")
        a = 10
        print("Initial:", a)
        a += 5
        print("a += 5:", a)
        a -= 3
        print("a -= 3:", a)
        a *= 2
        print("a *= 2:", a)
        a /= 4
        print("a /= 4:", a)
        a %= 3
        print("a %= 3:", a)
        a **= 2
        print("a **= 2:", a)
        a //= 2
        print("a //= 2:", a)
        print()

    # 5. Identity Operators
    def identity_operators(self):
        print("=== Identity Operators ===")
        a = [1, 2, 3]
        b = a
        c = [1, 2, 3]
        print("a is b:", a is b)
        print("a is c:", a is c)
        print("a == c:", a == c)
        print()

    # 6. Membership Operators
    def membership_operators(self):
        print("=== Membership Operators ===")
        my_list = [1, 2, 3, 4, 5]
        print("3 in list:", 3 in my_list)
        print("6 in list:", 6 in my_list)
        print("2 not in list:", 2 not in my_list)
        print("7 not in list:", 7 not in my_list)
        print()

    # 7. Bitwise Operators
    def bitwise_operators(self):
        print("=== Bitwise Operators ===")
        a = 5
        b = 3
        print("a & b:", a & b)
        print("a | b:", a | b)
        print("a ^ b:", a ^ b)
        print("~a:", ~a)
        print("a << 1:", a << 1)
        print("a >> 1:", a >> 1)
        print()

    # 8. Ternary Operator
    def ternary_operator(self):
        print("=== Ternary Operator ===")
        age = 18
        status = "Adult" if age >= 18 else "Minor"
        print("Status:", status)
        print()

    # 9. Walrus Operator
    def walrus_operator(self):
        print("=== Walrus Operator ===")
        if (n := len("Hello")) > 5:
            print("Greater")
        else:
            print("Length is:", n)
        print()


# Main Execution
if __name__ == "__main__":
    demo = OperatorsDemo()
    demo.arithmetic_operators()
    demo.comparison_operators()
    demo.logical_operators()
    demo.assignment_operators()
    demo.identity_operators()
    demo.membership_operators()
    demo.bitwise_operators()
    demo.ternary_operator()
    demo.walrus_operator()