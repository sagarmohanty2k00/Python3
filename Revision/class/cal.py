class Nums:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return (self.a + self.b)
    
nums = Nums(5, 7)

print(nums.a)
print(nums.b)
print(nums.add())


