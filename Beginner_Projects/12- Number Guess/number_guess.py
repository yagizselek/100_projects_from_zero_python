import random

from art import logo

def attempt_count(easy_or_hard):
    if easy_or_hard == "hard":
        return 5
    else:
        return 10

def game():
    print(logo)
    print("Hello, Let's play number guessing game!\nI'm thinking a number between 1 and 100")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = attempt_count(difficulty)
    hidden_number = random.choice(range(2, 100))
    while attempts != 0:
        print(f"you have {attempts} guesses left")
        guessed_number = int(input("Make a guess: "))
        attempts -= 1
        if guessed_number > hidden_number:
            print("Too high.")
        elif guessed_number < hidden_number:
            print("Too low.")
        else:
            print(f"Congrats! The answer was {hidden_number}")
            break
    if attempts == 0:
        print(f"You've run out of guesses, you lose. The number was {hidden_number}")

game()

