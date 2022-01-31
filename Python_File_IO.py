def save(room):
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Would you like to (s)ave, save and e(x)it, or anything else to cancel.")
    answer = input()
    if answer == "s":
        saveFile = open('save.txt', 'w')
        saveFile.write(str(room))
        saveFile.close()
        return ""
    elif answer == "x":
        saveFile = open('save.txt', 'w')
        saveFile.write(str(room))
        saveFile.close()
        return "q"
    else:
        return ""

room = 1 
answer = 'a' #dummy initialization 

answer = input("Would you like to (l)oad from your save? If not, press enter. ")
if answer == "l":
    saveFile = open('save.txt', 'r')
    room = int(saveFile.read())
    saveFile.close()

print ("Welcome. Explore the map. press 'q' to quit, or 's' to save.") 
while answer != 'q': 
    print ("Press 'q' to quit, or 's' to save.")
    if room == 1: 
        print ("You are in room 1, you can go E")
        answer = input() 
        if answer == "E": 
            room = 2 
        elif answer == "s":
            answer = save(room)
    elif room == 2: 
        print ("You are in room 2, you can go W or S") 
        answer = input() 
        if answer == "W": 
            room =1 
        elif answer == "S": 
            room =3 
        elif answer == "s":
            answer = save(room)
    elif room == 3: 
        print ("You are in room 3, you can go N or E") 
        answer = input () 
        if answer == "N": 
            room = 2 
        elif answer == "E": 
            room = 4 
        elif answer == "s":
            answer = save(room)
    elif room == 4: 
        print ("You are in room 4, you can go W") 
        answer = input() 
        if answer == "W": 
            room = 3 
        elif answer == "s":
            answer = save(room)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


