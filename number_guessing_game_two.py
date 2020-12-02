# !/usr/bin/env python

# Created by Larry Nkengbeza
# Created on December 2020
# This program is a guessing game program

import constants


def main():
    # This function makes user guess a number which will be correct.
    # Input
    random_number = int(input("Enter the random number: "))
    print("")
    # Process and Output
    if random_number == 4:
        print("Exactly the right number!")
    else:
        print("Not the right number. The correct number was 2")


if __name__ == "__main__":
    main()
