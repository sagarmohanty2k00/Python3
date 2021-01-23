# Series sum = 1 + 1/2! + 1/3! + ... + 1/n!

n = int(input("Enter The Value of n : "))

fact = 1
i = 1
sum = 0

while(i <= n):
    fact *= i
    sum += 1/fact
    i += 1

print(sum)

