# Series = sum = 1 + 1/2 + 1/3 + 1/3 + ...... + 1/n
n = int(input("Enter the value of n : "))

sum = 0
while(n>0):
    sum += 1/n
    n -= 1

print(sum)