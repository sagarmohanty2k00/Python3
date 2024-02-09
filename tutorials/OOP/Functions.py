def notGoing(): # user defined function
    print("Not going to school.")
    print("Going oidhuiohdfoh to play")
    print("Going to sleep")


def pieChart(a, b, c):
    _a = (a / (a+b+c)) * 100
    _b = (b / (a+b+c)) * 100
    _c = (c / (a+b+c)) * 100

def pieChartAdvanced(itemsList):
    _itemsList = []
    sum = 0
    for num in itemsList:
        sum += num
    
    for num in itemsList:
        _itemsList.append((num / sum) * 100)


raining = False
homeworkComplete = False

if raining:
    notGoing()
elif not homeworkComplete:
    notGoing()
else:
    print("Going to school.") # default function