import random
import hangman_words
import hangman_art

lives = 6
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)
word_length = len(chosen_word)
placeholder = list("_" * word_length)
print("Word to guess: " + "".join(placeholder))
game_over = False
correct_letters = []
guess = ""
guesses = []
while not game_over:
    if guess != "":
        print(f"**************************** {lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    checker = 0
    for i in range(word_length):
        if guesses.__contains__(guess):
            print(f"You've already guessed {guess}")
            break
        elif chosen_word[i] == guess:
            placeholder[i] = guess
        else:
            checker += 1
    guesses.append(guess)
    if checker == word_length:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    checker = 0
    print("Word to guess: " + "".join(placeholder))
    print(hangman_art.stages[lives])
    if lives == 0:
        game_over = True
        print(f"***********************IT WAS {chosen_word}! YOU LOSE**********************")
    if "_" not in placeholder:
        game_over = True
        print("****************************YOU WIN!****************************")


