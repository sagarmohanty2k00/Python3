# range function
# range returns a list of numbers
# range(10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(10):
    print(i, end=", ")
print()

for i in range(12, 15):
    print(i, end=", ")
print()

_list = ["acb", 45, 45.44, True]
for item in _list:
    print(item, end=", ")
print()

for index in range(len(_list)):
    print(_list[index], end=", ")
print()

_dict = {
    "1": 1,
    "2": 2
}
print(_dict.keys())
for key in list(_dict.keys()):
    print(_dict[key], end=", ")
print()


# numbers 1 - 100
# print all odds
# print first 10 odds

for num in range(1, 101):
    if num % 2 == 1:
        print(num)

for num in range(1, 101):
    if num % 2 == 0:
        continue

    print(num)

oddCount = 0
for num in range(1, 101):
    if num % 2 == 0:
        continue
    
    if oddCount < 10:
        print(num)
        oddCount += 1

oddCount = 0
for num in range(1, 101):
    if num % 2 == 0:
        continue
    
    print(num)
    oddCount += 1
    if oddCount >= 10:
        break

print(range(10))