#Rock,Paper,Scissors Game
import random 

def comp_choice():
    choices = ["rock","paper","scissor"]
    return random.choice(choices)

def winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a Tie"
    
    elif (user_choice == 'rock' and computer_choice=='scissor'):
        return "You Win"
    
    elif (user_choice == 'paper' and computer_choice=='rock'):
        return "You Win"

    elif (user_choice == 'scissor' and computer_choice=='paper'):
        return "You Win"    
    
    else:
        return "Computer Win"
    
def play():
    while True:
        user_choice = input("Enter a choice : 'rock','paper,'scissor or ('quit' to stop playing) : ").lower()

        if user_choice == 'quit':
            print("Thanks for playing")
            break

        if user_choice not in ['rock','paper','scissor']:
            print("Invalid choice.Enter a valid choice")
            continue

        computer_choice = comp_choice()
        print(f"Computer Chose : {computer_choice}")
        print(f"User Chose : {user_choice}")

        result = winner(user_choice,computer_choice)
        print(result)

play()
