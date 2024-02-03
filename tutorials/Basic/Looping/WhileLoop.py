running = True
miles = 0

while running:
    print("Drinking water..........")

    # increamenting velues relevant to breaking condition
    miles += 1

    # breaking condition - Most Important
    if miles == 10:
        break

# infinite loop - very bad
while running:
    print("running.........")