import messages as msg
import random

choices = ['rock', 'paper', 'scissors']
computer = random.choice(choices)
player = None
msg.Hello()

while player not in choices:
    player = input("Choose rock, paper, or scissors: ").lower()
    
if player == computer:
    print("Computer chose", computer)
    print("Player chose", player)
    print("Tie!") 
       
elif player == 'rock':
    if computer == 'paper':
        print("Computer chose", computer)
        print("Player chose", player)
        print("You lose!")
    if computer == 'scissors':
        print("Computer chose", computer)
        print("Player chose", player)
        print("You win!")
elif player == 'paper':
    if computer == 'rock':
        print("Computer chose", computer)
        print("Player chose", player)
        print("You win!")
    if computer == 'scissors':
        print("Computer chose", computer)
        print("Player chose", player)
        print("You lose!")
elif player == 'sicssors':
    if computer == 'paper':
        print("Computer chose", computer)
        print("Player chose", player)
        print("You win!")
    if computer == 'rock':
        print("Computer chose", computer)
        print("Player chose", player)
        print("You lose!")        
        
msg.Bye()