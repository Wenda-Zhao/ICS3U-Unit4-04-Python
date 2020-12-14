#!/usr/bin/env python3

# Created by: Wenda Zhao
# Created on: Dec 2020
# This program for break


import random


def main():
    # this function for break
    some_variable = random.randint(0, 9)   # a number between 0 and 9

    # input
    your_number = input("Enter your number (between 0 and 9): ")
    print("")

    # process & output
    try:
        your_number_int = int(your_number)
        while (True):
            if your_number_int == some_variable:
                print("your are correct\nDone!")
                break
            else:
                your_number_int = int(input("You are wrong, enter again: "))
    except Exception:
        print("It is not a integer")


if __name__ == "__main__":
    main()
