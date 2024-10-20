# tips
# if there is no wall at right, turn right
# if not, go straight
# if both right and straight are walls, turn left

def turn_right():
    for i in range(3):
        turn_left()


def move_safely():
    if front_is_clear():
        move()


x = 0

while x <= 4 and not wall_on_right():
    turn_left()
    x += 1
    if x == 4:
        move()
        x == 0

while not at_goal():
    if wall_on_right() and wall_in_front():
        turn_left()
        move_safely()
    elif wall_on_right():
        move_safely()
    else:
        turn_right()
        move_safely()