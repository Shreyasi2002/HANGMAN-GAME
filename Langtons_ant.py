from karel.stanfordkarel import *


def main():
    i = 0
    while True:  # repeat
        i = i + 1
        if beepers_present():  # At a black square
            pick_beeper()  # flip the color of the square
            turn_left()  # turn 90° left
            move()  # move forward one unit
        else:  # At a white square
            put_beeper()  # flip the color of the square
            turn_right()  # turn 90° right
            move()  # move forward one unit

        if i == 11000:
            break


def turn_right():
    for i in range(3):
        turn_left()


if __name__ == "__main__":
    run_karel_program('2x8.w')
