import random

words = ["lorem", "sagar", "I", "rourkela", "India", "We", '!', "is", "am", "are"]

n = int(input("lorem"))

print("lorem", end=" ")
for i in range(n-1):
    print( words[random.randint(0, 9)] , end=" ")


print()


