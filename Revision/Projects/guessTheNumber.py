import random


start = 1
end = 100


number = random.randint(start, end)


def suggestion(ip, number):
    if ip < number:
        if number % ip == 0:
            print("Multiply Something...")
        else:
            print("Add Something...")
    
    else:
        if ip % number == 0:
            print("Devide By Something...")
        else:
            print("Remove Something...")



ip = int(input("Guess a Number : "))
while(ip != number):
    suggestion(ip, number)
    ip = int(input("Guess a Number : "))


print("Congrats!!! You guessed the correct number ^_^ ")