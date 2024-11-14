#Number guessing game
import random

def guess_num():
    g_num = random.randint(1,100)
    guess = 0 
    print("I am thinking of a number between 1 and 100.Try to guess it")

    while guess != g_num:
        try:
            guess = int(input("Enter your guess :"))

            if guess < 1 or guess >100:
                print("Please enter a number between 1 and 100")
                continue

            if guess < g_num:
                print("Too low Try again")

            elif guess > g_num:
                print("Too high Try again")
            
            else:
                print(f"Congratulations! You guessed correct number : {g_num} ")

        except ValueError:
            print("Invalid Input.Please enter the valid integer")

guess_num()
