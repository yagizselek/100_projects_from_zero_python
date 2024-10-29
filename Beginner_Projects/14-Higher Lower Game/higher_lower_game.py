import random
import art
import game_data

game = True
current_score = 0

def get_data():
    data = random.choice(game_data.data)
    return {
        "name": data["name"],
        "description": data["description"],
        "country": data["country"],
        "followers": data["follower_count"],
    }

def check_answer(answer_a_b, compare_a, compare_b):
    if answer_a_b.lower() == "a" and compare_a > compare_b \
            or answer_a_b.lower() == "b" and compare_b > compare_a:
        return True
    else:
        return False


while game:
    print("\n" * 100)
    print(art.logo)
    if current_score != 0:
        print(f"You're right! Current score: {current_score}")
    else:
        first_data = get_data()
    second_data = get_data()
    print(f"Compare A: {first_data["name"]}, {first_data["description"]}, from {first_data["country"]}")
    print(art.vs)
    print(f"Against B: {second_data["name"]}, {second_data["description"]}, from {second_data["country"]}")
    answer = str(input("Who has more followers? Type 'A' or 'B': "))
    if check_answer(answer, first_data["followers"], second_data["followers"]):
        current_score += 1
        first_data = second_data
    else:
        game = False

print("\n" * 100 + art.logo + "\n" + f"Sorry, that's wrong. Final score: {current_score}")