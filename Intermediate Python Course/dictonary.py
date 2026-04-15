# A dictionary is an unordered collection of key-value pairs.
# Dictionaries are defined using curly braces {} and each key-value pair is separated by a colon :.
# Keys in a dictionary must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type.
# Dictionaries are commonly used for storing and retrieving data based on a unique key.
# Properties
# ✔ Unordered
# ✔ Mutable
# ✔ Keys are unique
# ✔ Values can be of any data type
# Explanation
# {} → used to create dictionary
# [] → used to access value by key
# 1. Creating a Dictionary
my_dict = {"name": "Alice", "age": 30, "city": "New York"}

# Accessing Values
print(my_dict["name"])  # Output: Alice
print(my_dict["age"])   # Output: 30

# Adding or Updating Elements
my_dict["email"] = "alice@example.com"  # Adding new key-value pair
my_dict["age"] = 31  # Updating existing value

# Removing Elements
del my_dict["city"]  # Removes the key-value pair with key "city"

# Looping through Dictionary
for key in my_dict:
    print(key, my_dict[key])

for key, value in my_dict.items():
    print(key, value)
