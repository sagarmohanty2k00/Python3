# Series sum = 1 + x + x^2/2! + x^3/3! + .... + x^n/n!

x = int(input("Enter the value of x : "))
n = int(input("Enter the value of n : "))

fact = 1
power = 1
i = 1
sum = 1

print(sum, end="")
while i<=n:

    power *= x
    fact *= i
    sum += power/fact
    print(" + " + str(power) + "/" + str(fact), end="")
    i += 1

print(" = " + str(sum))
