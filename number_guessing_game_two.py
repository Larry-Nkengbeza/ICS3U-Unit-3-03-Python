#  !/usr/bin/env python

# Created by Larry Nkengbeza
# Created on December 2020
# This program is a guessing game program

import random


def main():
    # This function makes user guess number which will be correct.

    # Input
    user_guess = int(input("Enter the random number: "))
    print("")
    computer_answer = random.randint(0, 9)

    # Process and Output
    if user_guess == random.randint(0, 9):
        # a number between 0 and 9
        print("Exactly the right number!")
    else:
        print("Wrong number. The correct number is {0}"
              .format(computer_answer))


if __name__ == "__main__":
    main()
