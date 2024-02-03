raining = False
homeworkComplete = False

if raining:
    print("Not going to school.")
elif not homeworkComplete:
    print("Not going to school.")
else:
    print("Going to school.")


if raining or not homeworkComplete:
    print("Not going to school.")
else:
    print("Going to school.")


if not raining and homeworkComplete:
    print("Going to school.")
else:
    print("Not going to school.")