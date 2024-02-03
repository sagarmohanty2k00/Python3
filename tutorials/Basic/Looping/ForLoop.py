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

print(range(10))