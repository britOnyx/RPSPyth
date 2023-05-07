'''
Created on 28 Aug 2020

@author: suresh
'''
import random


#FUNCTIONS NEED TO BE DECLARED FIRST
def generateNewObJ():
    RPSlist=[]

    RPSlist.append("rock")
    RPSlist.append("paper")
    RPSlist.append("scissors")
    
    intNumber = random.randrange(0,3)
    
    print("Opponent: " + RPSlist[intNumber])
    
    return RPSlist[intNumber]
    

def viewScoreBoard():
    scoreBoard = [["ID: " "Name: ", "Score:"], ["1.", "Michael", "20"]]
    
    print("---------------------------")
    print("Score Board:")
    
    for a in scoreBoard:
        for b in a:
            print(b,end = "  ")
        print()
    
print("Rock, Paper, Scissors Game")
print("---------------------------")


end = False
intscore = 0

while end == False:
    print("Score : ", intscore);
    
    answer = generateNewObJ()
    
    myinput = (input("Input Object (Rock, Paper or Scissors): \n")).lower()
    
    if not myinput:
        raise ValueError('empty string');
    elif myinput == "rock" and answer == "scissors" or myinput == "paper" and answer == "rock" or myinput == "scissors" and answer == "paper":
        
        print("You Win!");
        intscore += 1;
    elif myinput == answer:
        print("This is a draw!");
    else:
        print("You Loose!");            
        
    inputYN = input("Do you want to play again?: \n").lower();
    
    if inputYN == "n" or inputYN == "no":
        end = True;
        print("Game Over!\nYour score is:", intscore);
        
        viewScoreBoard()