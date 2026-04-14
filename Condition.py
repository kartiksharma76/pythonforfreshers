# ================= CONDITIONAL STATEMENTS (IF-ELSE) =================

# Conditional statements are used to make decisions in a program.
# They execute different blocks of code based on conditions.
class ConditionalDemo:

    def run(self):

        print("=== Conditional Statements Demo ===")


        # ------------------------------------------------------------------
        # 1. Simple IF Statement:
        # Executes code only when condition is True

        age = 20

        # Condition: age >= 18 (checks if age is greater than or equal to 18)
        if age >= 18:
            # This block runs only if condition is True
            print("You are an adult")


        # ------------------------------------------------------------------
        # 2. IF-ELSE Statement:
        # Used when there are two possible outcomes

        num = 7

        # Condition: check even or odd
        if num % 2 == 0:
            # Runs if condition is True
            print("Even Number")
        else:
            # Runs if condition is False
            print("Odd Number")


        # ------------------------------------------------------------------
        # 3. IF-ELIF-ELSE Statement:
        # Used for multiple conditions

        marks = 85

        if marks >= 90:
            # Runs if marks >= 90
            print("Grade A")

        elif marks >= 75:
            # Runs if first condition is False and this is True
            print("Grade B")

        elif marks >= 50:
            # Runs if above conditions are False
            print("Grade C")

        else:
            # Runs if all conditions are False
            print("Fail")


        # ------------------------------------------------------------------
        # 4. Nested IF:
        # One if statement inside another if

        age = 22

        if age >= 18:
            # First condition is True
            if age >= 21:
                # Second condition inside first if
                print("Eligible for driving + drinking")
            else:
                print("Eligible for driving only")
        else:
            print("Not eligible")


        # ------------------------------------------------------------------
        # 5. User Input Example:
        # Taking input and applying conditions

        number = int(input("Enter a number: "))

        if number > 0:
            print("Positive Number")

        elif number < 0:
            print("Negative Number")

        else:
            print("Zero")


# ---------------- MAIN ----------------
# Creating object of class
obj = ConditionalDemo()

# Calling run method
obj.run()