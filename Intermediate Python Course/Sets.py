# A set is an unordered collection of unique elements.
# Sets are defined using curly braces {} and elements are separated by commas.
# Sets do not support indexing or slicing because they are unordered.
# Sets are commonly used for membership testing, removing duplicates from a collection, and performing mathematical set operations like union, intersection, and difference.
# Properties
# ✔ Unordered
# ✔ Mutable
# ✔ No duplicates
# Explanation
# {} → used to create set
# add() → adds element to set
# remove() → removes element from set
# 1. Creating a Set
# Creating set
my_set = {1, 2, 3, 4}

# Adding element
my_set.add(5)

# Removing element
my_set.remove(2)

# Duplicate not allowed
my_set.add(3)

# Looping
for item in my_set:
    print(item)

