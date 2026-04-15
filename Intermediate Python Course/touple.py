# touple is a an ordered immutable (unchangeable) collection of elements.
# Tuples can contain elements of different data types (e.g., integers, strings, etc.).
# Tuples are defined using parentheses () and elements are separated by commas.
# Tuples support indexing (accessing elements by position) and slicing (accessing a range of elements).
# Tuples are commonly used for storing fixed collections of data that should not be modified.
# Properties
# ✔ Ordered
# ✔ Immutable
# ✔ Allows duplicates
# ✔ Can store multiple data types
# Explanation
# () → used to create tuple
# Index starts from 0
# 1. Creating a Tuple
my_tuple = (1, 2, 3, "hello", 4.5)

# 2. Accessing Elements
print(my_tuple[0])  # Output: 1 (first element)
print(my_tuple[3])  # Output: hello (fourth element)

# 3. Tuples are immutable, so we cannot add or remove elements
# my_tuple.append(50)  # This will raise an error because tuples do not have an append method
# my_tuple.insert(2, "new")  # This will raise an error because tuples do not have an insert method
# my_tuple.remove("hello")  # This will raise an error because tuples do not have
# a remove method
# loop through tuple

for item in my_tuple:
    print(item)

#  touple unpacking
a, b, c, d, e = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3
print(d)  # Output: hello
print(e)  # Output: 4.5