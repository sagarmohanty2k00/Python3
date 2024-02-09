for number in range(2, 101):
    divCount = 0
    for div in range(2,  number):
        if number % div == 0:
            divCount += 1
            break

    if divCount == 0:
        print(number, end=" ")
print()