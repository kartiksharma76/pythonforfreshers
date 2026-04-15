class Father:
    def skill1(self):
        print("Driving")
class Mother:
    def skill2(self):
        print("Cooking")

class Child(Father, Mother):
    def skill3(self):
        print("Programming")

child = Child()
child.skill1()  # Output: Driving
child.skill2()  # Output: Cooking
child.skill3()  # Output: Programming