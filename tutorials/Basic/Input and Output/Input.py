print("Enter Your Name: ")
name = input()
print(name)

name = input("Enter your name: ")
print(name)

# Note: input function can only take string inputs

number = input("Enter a number: ")
print(number)
print(type(number))

# Note convert all values according to youlr usecase

number = int(input("Enter a number: "))
print(number)
print(type(number))

# Note list input

_list = list(map(int, input("list(comma separated values only): ").split(",")))
print(_list)
print(type(_list))