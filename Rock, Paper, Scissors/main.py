#Gavin Pierce Rock, Paper, Scissors
import random
playerScore= 0
aiScore= 0
playChoiseList=["rock", "paper", "sicssors"]
likeToPlay=input("hi there I am the rock paper scissors bot would you like to play? ")

if likeToPlay == "yes":
    print("ok" )
    while likeToPlay == "yes":
        playChoise=input("what would you like to chose? rock, paper or sicssors? ")
        if playChoise in playChoiseList:
            aiTurn= random.choice(playChoiseList)

            
            if playChoise == "rock": 
                if aiTurn == "sicssors":
                    print("you won")
                    playerScore += 1
                    print("the score is", playerScore, "to", aiScore)
                    likeToPlay=input("would you like to play again? ")
                
                elif aiTurn == "rock": 
                    print("you tied")
                    print("the score is", playerScore, "to", aiScore)
                    likeToPlay=input("would you like to play again? ")
                    
                else:
                    print("the ai won")
                    aiScore += 1
                    print("the score is", playerScore, "to", aiScore)
                    likeToPlay=input("would you like to play again? ")


            if playChoise == "paper": 
                if aiTurn == "rock":
                    print("you won")
                    playerScore += 1
                    print("the score is", playerScore, "to", aiScore)
                    likeToPlay=input("would you like to play again? ")

                elif aiTurn == "paper":
                     print("you tied")
                     print("the score is", playerScore, "to", aiScore)
                     likeToPlay=input("would you like to play again? ")
                    
                else: 
                    print("the ai won")
                    aiScore += 1
                print("the score is", playerScore, "to", aiScore)         
                likeToPlay=input("would you like to play again? ")


            if playChoise == "sicssors": 
                if aiTurn == "paper":
                    print("you won")
                    playerScore += 1
                    print("the score is", playerScore, "to", aiScore)
                    likeToPlay=input("would you like to play again? ")

                elif aiTurn == "sicssors":
                    print("you tied")
                    print("the score is", playerScore, "to", aiScore)
                    likeToPlay=input("would you like to play again? ")
                                
                else: 
                    print("the ai won")
                    aiScore += 1
                    print("the score is", playerScore, "to", aiScore)
                    likeToPlay=input("would you like to play again? ")    
  
else: print("OK bye :(")