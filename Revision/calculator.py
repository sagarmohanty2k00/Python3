# Calculator program
def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b


while True:
    a = int(input("Enter a num: "))
    b = int(input("Enter another num: "))

    c = input("Enter the fun: ")

    if c == '+':
        print(add(a, b))
    elif c == '-':
        print(sub(a, b))
    elif c == '*':
        print(mul(a, b))

    else:
        print("ERROR...")