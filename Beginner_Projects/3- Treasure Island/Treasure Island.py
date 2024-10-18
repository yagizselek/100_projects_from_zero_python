
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

second_choice = ""
third_choice = ""


first_choice = input("As soon as you land on the island you look around and "
                     "on the left side there is a deserted road "
                     "and on the right side there is a big forest. "
                     "Which way do you go?\n"
                     "Type 'Left' for left or 'Right' for right. ")

if first_choice == "Left":
        second_choice = input("You moved on the road and nothing happened to you. "
              "Now there is a river in front of you, do you swim across or "
              "wait for a boat to come?\n"
              "Type 'Swim' for swim across or 'Wait' for wait")
elif first_choice == "Right":
        print("You were attacked by wolves as you were traveling through the forest.\n"
              "Game Over.")
        exit()
else:
        print("You typed wrong input. Start again.")
        exit()

if second_choice == "Wait":
    third_choice = input("Luckily a boat came and took you across. "
                         "Now you enter a temple and there are three doors: "
                         "Red, blue and yellow. "
                         "Which door will you go through?\n"
                         "Type 'Red' , 'Blue' or 'Yellow'")
elif second_choice == "Swim":
    print("You could not resist the strong current of the river and you were swept away and died.\n"
          "Game Over.")
    exit()
else:
    print("You typed wrong input. Start again.")

if third_choice == "Red":
    print("The moment you touched the door handle, the room exploded and you died.\n"
          "Game Over.")
elif third_choice == "Blue":
    print("You walked through the door and as you moved towards the treasure in front of you, "
          "a poisonous gas surrounded you. The treasure was fake and you died of poisoning."
          "Game Over.")
elif third_choice == "Yellow":
    print("You walked through the door and the room was full of treasure!\n"
          "Congratulations on your win.")
else:
    print("You typed wrong input. Start again.")
