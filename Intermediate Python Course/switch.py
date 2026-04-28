print("1. Even odd")
print("2. Star pattern")
print("3. Table print")

try:
    choice = int(input("enter a choice: "))
    match choice:
        case 1:
            
            # even odd
            num = int(input("enter a number: "))
            if num % 2 == 0:
                print("even")
            else:
                print("odd")

        case 2: 
            # star pattern 
            for i in range(5):
                for j in range(i+1):
                    print("*", end="")
                print()

        case 3:
            # table print
            num = int(input("enter a number: "))
            for i in range(1, 11):
                print(num, "x", i, "=", num*i)

        case _:
            print("Invalid choice")
except ValueError:
    print("Error: Please enter only an integer.")