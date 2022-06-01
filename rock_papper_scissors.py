from random import randint

#create a list of play options
t = ["R", "P", "S", "END"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("R, P, S, END?")
    if player == computer:
        print("Tie!")
    elif player == "R":
        if computer == "P":
            print("You lose!", "CPU =", computer, "covers", "PLAYER = ",player)
        else:
            print("You win!", "PLAYER = ", player, "smashes", "CPU =",computer)
    elif player == "P":
        if computer == "S":
            print("You lose!", "CPU =", computer, "cut", "PLAYER = ",player)
        else:
            print("You win!", "PLAYER = ", player, "covers", "CPU =",computer)
    elif player == "S":
        if computer == "R":
            print("You lose...", "CPU =",computer, "smashes", "PLAYER = ",player)
        else:
            print("You win!", "PLAYER = ", player, "cut", "CPU =", computer)
    elif player == "END":
        break
    else:
        print("That's not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]