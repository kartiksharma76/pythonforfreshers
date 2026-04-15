# A List is an ordered, mutable (changeable) collection of elements.
# Lists can contain elements of different data types (e.g., integers, strings, etc.).
# Lists are defined using square brackets [] and elements are separated by commas.
# Lists support indexing (accessing elements by position) and slicing (accessing a range of elements).
# Lists are commonly used for storing and manipulating collections of data.

# Properties

# ✔ Ordered
# ✔ Mutable
# ✔ Allows duplicates
# ✔ Can store multiple data types


# Explanation
# [] → used to create list
# Index starts from 0
# append() → adds element at end
# insert() → adds at specific index
# remove() → deletes element

# 1. Creating a List
my_list = [1, 2, 3, "hello", 4.5]
# 2. Accessing Elements
print(my_list[0])  # Output: 1 (first element)
print(my_list[3])  # Output: hello (fourth element)

# 3. Adding elements
my_list.append(50)
print(my_list)  # Output: [1, 2, 3, 'hello', 4.5, 50]
my_list.insert(2, "new")
print(my_list)  # Output: [1, 2, 'new', 3, 'hello', 4.5, 50]

# 4. inserting elements
my_list.insert(2, "new")
print(my_list)  # Output: [1, 2, 'new', 3


# 5. Removing elements
my_list.remove("hello")  # This will raise an error because "Hello kartik" is not in the list
print(my_list)  # Output: [1, 2, 'new', 3, 'hello', 4.5, 50]
# loop through list 
for item in my_list:
    print(item) 

