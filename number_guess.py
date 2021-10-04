#!/usr/bin/env python3

# Created by: Liam Fletcher
# Created on: Oct 2021
# This program asks the user to guess a number between 0 - 9

import random


def main():
    # this tells the user if they picked the right number

    # input
    number_as_string = input("Enter a number between 0 - 9 : ")
    random_as_number = random.randint(1, 9)  # a number between 1 and 9

    # process & output
    try:
        integer_as_number = int(number_as_string)

        while True:
            if integer_as_number < 0:
                print("This is not a positive number!")
            else:
                if integer_as_number == random_as_number:
                    print("You gussed the number correctly!")
                    break
                if integer_as_number > random_as_number:
                    print("Wrong, You guessed too high!")
                    # integer_as_number = input("Try another guess: ")
                if integer_as_number < random_as_number:
                    print("Wrong, You guessed too low!")
                    # integer_as_number = input("Try another guess: ")
                    # print("You guessed too low!")

            number_as_string = input("Try another guess: ")
            integer_as_number = int(number_as_string)

    except Exception:
        print("This is a invaild number!")

    finally:
        print("Thank you for playing!")


if __name__ == "__main__":
    main()
