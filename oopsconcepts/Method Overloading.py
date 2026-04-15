class Math:
    def add(self, a, b=0, c=0):
        return a + b + c

obj = Math()
print(obj.add(5))
print(obj.add(5, 10))
print(obj.add(5, 10, 15))