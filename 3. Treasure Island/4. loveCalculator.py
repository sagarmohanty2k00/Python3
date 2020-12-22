# Program for Love Calculator, By - Sagar Mohanty

print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is his/her name? ").lower()

combinedName = name1 + name2

t = combinedName.count('t')
r = combinedName.count('r')
u = combinedName.count('u')
e = combinedName.count('e')

true = t + r + u + e

l = combinedName.count('l')
o = combinedName.count('o')
v = combinedName.count('v')
e = combinedName.count('e')

love = l + o + v + e

score =( true*10 + love )%101
print("\nYour score is "+str(score)+'%', end=', ')


if(score < 10 or score > 90):
    print('you go together like coke and mentos.\n')

elif(score < 50 or score > 40):
    print('you are right together.\n')

if(score < 10 or score > 90):
    print('\n')