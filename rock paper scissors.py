import random 

choices = ["rock", "paper", "scissors"]

loop = True
userScore = 0
computerScore = 0

while(loop == True):
    #checks to see if user or computer has won (3 points)
    if userScore == 3 or computerScore == 3:
        if(userScore > computerScore):
            print("Game over, you have beat the computer")
        else:
            print("Game over, computer won")

        playAgain = input("\nplay again (y or n): ")
        if(playAgain == "y"):
            userScore = 0
            computerScore = 0
        else:
            break


    computerChoiceIndex = random.randrange(0,len(choices))
    computerChoice = choices[computerChoiceIndex]
    userChoice = input("(rock, paper, or scissors): ")
    #if user picks rock 
    if(userChoice == "rock"):
        #user gets a point
        if(computerChoice == "scissors"):
            userScore += 1
            print("\ncomputer picked " + computerChoice)
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
        #no points given to either
        elif(computerChoice == "rock"):
            print("\ncomputer picked " + computerChoice + " also, no points given")
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
        #computer gets point
        elif(computerChoice == "paper"):
            computerScore += 1
            print("\ncomputer picked " + computerChoice)
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
    #if user picks paper 
    elif(userChoice == "paper"):
        #user gets a point
        if(computerChoice == "rock"):
            userScore += 1
            print("\ncomputer picked " + computerChoice)
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
        #no points given to either
        elif(computerChoice == "paper"):
            print("\ncomputer picked " + computerChoice + " also, no points given")
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
        #computer gets point
        elif(computerChoice == "scissors"):
            computerScore += 1
            print("\ncomputer picked " + computerChoice)
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
    #if user picks scissors 
    elif(userChoice == "scissors"):
        #user gets a point
        if(computerChoice == "paper"):
            userScore += 1
            print("\ncomputer picked " + computerChoice)
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
        #no points given to either
        elif(computerChoice == "scissors"):
            print("\ncomputer picked " + computerChoice + " also, no points given")
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
        #computer gets point
        elif(computerChoice == "rock"):
            computerScore += 1
            print("\ncomputer picked " + computerChoice)
            print("user score - " + str(userScore) + "\ncomputer score - " + str(computerScore) + "\n")
    else:
        print("error: unknown command")
        
   