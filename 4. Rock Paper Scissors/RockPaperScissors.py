# Implementation of Rock-Paper-Scissor using random module

import random

option = ['Rock', 'Scissors', 'Paper']

player = 0
computer = 0


rounds = 0

while rounds < 5:
    yourChoice = int(input('What is Your Choice :\n "1" for Rock\n "2" for Paper\n "3" for Scissors\n')) - 1
    computerChoice = random.randint(0, 2)


    if yourChoice == (computerChoice+1)%3 :
        print(f"Your have chosen: {option[yourChoice]} and computer had chosen: {option[computerChoice]}, so you loose.")
        computer = computer + 1

    else:
        print(f"Your have chosen: {option[yourChoice]} and computer had chosen: {option[computerChoice]}, so you win.")
        player = player + 1

    rounds = rounds + 1


print(f"Your Score = {player}")
print(f"Computer's Score = {computer}")