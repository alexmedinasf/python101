import messages as msg
import random

msg.Hello()
while True:
    
    choices = ['rock', 'paper', 'scissors']
    computer = random.choice(choices)
    player = None
    
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
            
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
            break            
        
msg.Bye()