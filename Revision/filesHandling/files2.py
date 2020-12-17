file = open("new_File.txt", 'r')

# print(file.read())

# print(file.readline())
# print(file.readline())

f = file.readlines()

for line in f:
    print(line)


