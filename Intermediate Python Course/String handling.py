# String Handling basically means working with strings. In Python, strings are a sequence of characters enclosed in either single quotes (' ') or double quotes (" ").
# Strings are immutable, which means that once a string is created, it cannot be changed.
# Properties
# ✔ Ordered
# ✔ Immutable
# ✔ Allows duplicates
# Explanation
# '' or "" → used to create string
# 1. Creating a String
class StringDemo:

    # 1. Basic String Creation
    def create_strings(self):
        name = "Kartik"
        msg = 'Hello'
        para = """This is a multi-line string"""
        print(name, msg)
        print(para)

    # 2. Indexing
    def indexing(self):
        text = "Python"
        print("First:", text[0])
        print("Last:", text[-1])

    # 3. Slicing
    def slicing(self):
        text = "Python"
        print("0:3 ->", text[0:3])
        print(":4 ->", text[:4])
        print("2: ->", text[2:])
        print("Reverse ->", text[::-1])

    # 4. String Operations
    def operations(self):
        a = "Hello"
        b = "World"
        print("Concat:", a + " " + b)
        print("Repeat:", a * 3)

    # 5. Case Conversion
    def case_methods(self):
        text = "python"
        print(text.upper())
        print(text.lower())
        print(text.capitalize())

    # 6. Searching
    def searching(self):
        text = "Hello Python"
        print("Find:", text.find("Python"))
        print("Count of o:", text.count("o"))

    # 7. Replace
    def replace_demo(self):
        text = "Hello Python"
        print(text.replace("Python", "Java"))

    # 8. Split and Join
    def split_join(self):
        text = "apple,banana,mango"
        data = text.split(",")
        print("Split:", data)
        print("Join:", "-".join(data))

    # 9. Strip (remove spaces)
    def strip_demo(self):
        text = "  Hello  "
        print("Strip:", text.strip())
        print("LStrip:", text.lstrip())
        print("RStrip:", text.rstrip())

    # 10. Check Functions
    def check_functions(self):
        text = "Python123"
        print("isalpha:", text.isalpha())
        print("isdigit:", text.isdigit())
        print("isalnum:", text.isalnum())

    # 11. String Formatting
    def formatting(self):
        name = "Kartik"
        age = 20
        print(f"My name is {name} and age is {age}")
        print("My name is {} and age is {}".format(name, age))

    # 12. Escape Characters
    def escape_demo(self):
        print("Hello\nWorld")
        print("Hello\tWorld")
        print("He said \"Hi\"")

    # 13. Looping
    def loop_demo(self):
        text = "Python"
        for ch in text:
            print(ch)

    # 14. Immutability Demo
    def immutability(self):
        text = "Python"
        text = "Jython"   # new string created
        print(text)


# ================= MAIN =================
if __name__ == "__main__":
    obj = StringDemo()

    obj.create_strings()
    obj.indexing()
    obj.slicing()
    obj.operations()
    obj.case_methods()
    obj.searching()
    obj.replace_demo()
    obj.split_join()
    obj.strip_demo()
    obj.check_functions()
    obj.formatting()
    obj.escape_demo()
    obj.loop_demo()
    obj.immutability()