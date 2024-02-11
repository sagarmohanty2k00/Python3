'''
8. *
   **
   ***
   ****
   *****
   .............. upto nth level

9. *
   **
   ***
   ****
   *****
   ****
   ***
   **
   *

10.   *
     **
    ***
   ****

'''

n = int(input("rows: "))

for row in range(n):
    for star in range(row+1):
        print("*", end=" ")
    print()

for row in range(n*2):
    if (row < n):
        for star in range(row+1):
            print("*", end=" ")
        print()

    else :
        for star in range(n - (row - n) - 1):
            print("*", end=" ")
        print()

for row in range(n):
    for space in range(n-1-row):
        print(" ", end=" ")
    for star in range(row+1):
        print("*", end=" ")
    print()

