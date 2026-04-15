# file handling in python
# File handling is a crucial aspect of programming that allows you to read from and write to files. In Python, you can use built-in functions to work with files. Here are some common file handling operations:    
# 1. Opening a file
# 2. Reading from a file    
# 3. Writing to a file
# 4. Closing a file
# 1. Opening a file
# You can open a file using the open() function, which takes the file name and mode as arguments. The mode can be 'r' for reading, 'w' for writing, 'a' for appending, and 'b' for binary mode.
# Example:
# file = open('example.txt', 'r')  # Open for reading
# 2. Reading from a file
# You can read the contents of a file using methods like read(), readline(), or readlines().

# Example:
# content = file.read()  # Read the entire file
# 3. Writing to a file
# You can write to a file using the write() method.
# Example:
# file = open('example.txt', 'w')  # Open for writing
# file.write('Hello, World!')  # Write to the file
# 4. Closing a file
# You should always close a file after you're done with it.
# Example:
# file.close()  # Close the fil

class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def write_to_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)

    def read_from_file(self):
        with open(self.filename, 'r') as file:
            return file.read()
        
# Example usage
file_handler = FileHandler('example.txt')
file_handler.write_to_file('Hello, World!') 
print(file_handler.read_from_file())  # Output: Hello, World!   
# In this example, we created a FileHandler class that encapsulates file handling operations. The write_to_file method writes content to the specified file, while the read_from_file method reads and returns the content of the file. The with statement is used to ensure that the file is properly closed after its suite finishes, even if an exception is raised. 

