_listOfNumbers = list(map(int, input("Enter your list(space separated): ").split(" ")))

_sum = 0
for number in _listOfNumbers:
    _sum += number

print(_sum)
