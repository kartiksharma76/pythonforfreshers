# ================= LOOPS IN PYTHON =================

# Loops are used to repeat a block of code multiple times.
# Two main types:
# 1. for loop
# 2. while loop


class LoopDemo:

    def run(self):

        print("=== Loops Demo ===")


        # ------------------------------------------------------------------
        # 1. FOR LOOP:
        # Used when number of iterations is known

        print("\n--- For Loop ---")

        # range(5) → generates numbers from 0 to 4
        for i in range(5):
            # This block runs 5 times
            print("Value of i:", i)


        # ------------------------------------------------------------------
        # FOR LOOP with range(start, end)

        print("\n--- For Loop with Range ---")

        # range(1, 6) → 1 to 5
        for i in range(1, 6):
            print(i)


        # ------------------------------------------------------------------
        # FOR LOOP with step

        print("\n--- For Loop with Step ---")

        # range(1, 10, 2) → 1, 3, 5, 7, 9
        for i in range(1, 10, 2):
            print(i)


        # ------------------------------------------------------------------
        # LOOP through LIST

        print("\n--- Loop through List ---")

        my_list = [10, 20, 30]

        for item in my_list:
            print("Item:", item)


        # ------------------------------------------------------------------
        # 2. WHILE LOOP:
        # Used when number of iterations is unknown

        print("\n--- While Loop ---")

        count = 1

        # Loop runs until condition becomes False
        while count <= 5:
            print("Count:", count)
            count += 1   # increment (important to avoid infinite loop)


        # ------------------------------------------------------------------
        # INFINITE LOOP (Example - careful ⚠️)

        # while True:
        #     print("This runs forever")   # infinite loop


        # ------------------------------------------------------------------
        # BREAK Statement:
        # Used to exit loop immediately

        print("\n--- Break Example ---")

        for i in range(1, 6):
            if i == 3:
                break   # stops loop when i = 3
            print(i)


        # ------------------------------------------------------------------
        # CONTINUE Statement:
        # Skips current iteration

        print("\n--- Continue Example ---")

        for i in range(1, 6):
            if i == 3:
                continue   # skip 3
            print(i)


        # ------------------------------------------------------------------
        # PASS Statement:
        # Does nothing (placeholder)

        print("\n--- Pass Example ---")

        for i in range(3):
            pass   # no operation


# ---------------- MAIN ----------------
obj = LoopDemo()
obj.run()