#Gavin Pierce Rock, Paper, Scissors
import random
playerScore= 0
aiScore= 0
playChoiseList=["rock", "paper", "sicssors"]
likeToPlay=input("hi there I am the rock paper scissors bot would you like to play? ")

if likeToPlay == "yes":
    print("ok" )
    playAgain="yes"
    while playAgain == "yes":
        playChoise=input("what would you like to chose? rock, paper or sicssors? ")
        if playChoise in playChoiseList:
            aiTurn= random.choice(playChoiseList)
            if playChoise == "rock": 
                if aiTurn == "scicssors":
                    print("you won")
                    playerScore += 1
                    print("the score is", playerScore, "to", aiScore)
                
                elif print("you tied"):
                     print("the score is", playerScore, "to", aiScore)
                else: print("the ai won")
                aiScore += 1    

            if playChoise == "paper": 
                if aiTurn == "rock":
                    print("you won")
                    playerScore += 1
                    print("the score is", playerScore, "to", aiScore)
                elif print("you tied"):

                     print("the score is", playerScore, "to", aiScore)
                else: print("the ai won")
                aiScore += 1         

            if playChoise == "sicssors": 
                if aiTurn == "paper":
                    print("you won")
                    playerScore += 1
                    print("the score is", playerScore, "to", aiScore)
                elif print("you tied"):

                     print("the score is", playerScore, "to", aiScore)                
                else: print("the ai won")
                aiScore += 1                        
                                
        else: print("you need a valid varible")
else: print("OK bye :(")