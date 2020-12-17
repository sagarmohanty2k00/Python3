import random

rooms = {
    "1":{
        "color": "Voulet",
        "structure": "square",
        "beds": "2 Beds",
        "bathroom": "No Bathroom",
        "toilet": "No Toilets",
        "story": "Mahatma Gandhi Lived Here...",
    },
    "2":{
        "color": "Neivy Blue",
        "structure": "Hexagon",
        "beds": "King Size Bed",
        "bathroom": "Very Big Bathroom",
        "toilet": "One Large Toilet",
        "story": "Modi Used To Make Out Here...",
    },
    "3":{
        "color": "Blue",
        "structure": "Triangle",
        "beds": "Khatia",
        "bathroom": "No Bathroom",
        "toilet": "No Toilets",
        "story": "Teenager's Room...",
    },
    "4":{
        "color": "Green",
        "structure": "Square",
        "beds": "Queen's Bed",
        "bathroom": "Big Bathroom",
        "toilet": "One Large Toilet",
        "story": "Princess Dyna Lived Here...",
    },
    "5":{
        "color": "Yellow",
        "structure": "Octagon",
        "beds": "No Beds",
        "bathroom": "No Bathrooms",
        "toilet": "No Toilets",
        "story": "Yellow is Safe Rest Here For Sometime...",
    },
    "6":{
        "color": "Orange",
        "structure": "Circle",
        "beds": "King Size Bed",
        "bathroom": "Very Big Bathroom",
        "toilet": "Two Large Toilets",
        "story": "You Are Close To The Finish...",
    },
    "7":{
        "color": "Red",
        "structure": "Pentagon",
        "beds": "2 King Size Beds",
        "bathroom": "Very Small Bathroom",
        "toilet": "One Small Toilets",
        "story": "Red Is The Simbol of Love You Will Find Your Love Here, Escape Early....",
    },
}

doors = {
    "1": [2, 3, 4],
    "2": [1, 5, 7],
    "3": [1, 6, 5],
    "4": [1, 7],
    "5": [2, 3],
    "6": [3, 7],
    "7": [2, 4, 6],
}


def describe_room(room, rooms):
    r = rooms[room]
    allkeys = r.keys()
    for i in allkeys:
        print(str(i) + " : " + str(r[i]))


def all_doors(room, doors):
    print("Enter The Room")
    for i in doors[room]:
        print(i, end=" ")

    print("")

escape_room = random.randint(1, 7)


room = input("Enter The Room\n 1 2 3 4 5 6 7\n")


while (str(escape_room) != room):
    describe_room(room, rooms)
    all_doors(room, doors)
    room = input()


print("You Have Successfully Escaped ^_^  ")
