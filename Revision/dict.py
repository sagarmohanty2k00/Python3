di = {}

singnedUp = False
while not singnedUp:
    key = input("key: ")
    value = input("value: ")

    di[ key ] = value

    ok = input("Sign Up Completed( Y or N ) : ")

    if ok == 'Y' :
        singnedUp = True

print(di)
    




