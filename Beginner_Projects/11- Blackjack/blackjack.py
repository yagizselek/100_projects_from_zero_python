import random

from art import logo


def final_text():
    print(
        f"       Your final hand: {player_deck}, final score: {player_score}\n   Computer's final hand: {computer_deck}, final score: {computer_score}")


def get_card(whose_deck):
    card = random.choice(whose_deck)
    whose_deck.remove(card)
    return int(card)


def what_is_player_score(boolean):
    """calculates the player_score and checks if it is greater than 21"""
    global player_score
    global wanna_play
    global draw
    player_score = 0
    for x in player_deck:
        player_score += x
    if boolean:
        if player_score > 21 and 11 in player_deck:
            player_deck[player_deck.index(11)] = 1
            what_is_player_score(True)
        elif player_score > 21:
            print("You went over. You lose 😭")
            wanna_play = "setup"
            draw = "no more"


def end_of_things():
    global draw
    print(f"    Your cards: {player_deck}, current score: {player_score}")
    print(f"    Computer's first hand: {computer_deck[0]}")
    if draw != "no more":
        draw = input("Type 'y' to get another card, type 'n' to pass: ")


def comp_turn():
    global computer_score
    global wanna_play
    computer_score = 0

    for x in computer_deck:
        computer_score += x
    if computer_score > 21 and 11 in computer_deck:
        computer_deck[computer_deck.index(11)] = 1
        if computer_score >= 17:
            comp_turn()
        else:
            computer_deck.append(get_card(computer_cards))
            comp_turn()
    elif computer_score > 21:
        final_text()
        print("Opponent went over. You win 😁")
        wanna_play = "setup"
    elif computer_score >= 17:
        if computer_score == player_score:
            final_text()
            print("Draw 🙃")
        elif computer_score > player_score:
            final_text()
            print("You lose 😤")
        else:
            final_text()
            print("You win 😃")
        wanna_play = "setup"
    else:
        computer_deck.append(get_card(computer_cards))
        comp_turn()


again = "a game of Blackjack"

while True:
    player_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    computer_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    player_deck = []
    computer_deck = []
    player_score = 0
    computer_score = 0
    draw = ""
    wanna_play = input(f"Do you want to play {again}? Type 'y' or 'n': ")
    while wanna_play == "y":
        print("\n" * 100 + logo)
        player_deck.append(get_card(player_cards))
        player_deck.append(get_card(player_cards))
        computer_deck.append(get_card(computer_cards))
        what_is_player_score(False)
        end_of_things()
        while draw == "y":
            player_deck.append(get_card(player_cards))
            what_is_player_score(True)
            end_of_things()
        if draw == "n":
            comp_turn()

    again = "again"