from math import trunc
import sys
from random import randint


def main():
    nb = randint(1, 99)
    print('''This is an interactive guessing game!
You have to enter a number between 1 and 99 to find out the secret number.
Type 'exit' to end the game.
Good luck!\n''')
    win = False
    c = 0
    while not win:
        guess = input("What's your guess between 1 and 99?\n>> ")
        c += 1
        if guess == 'exit':
            break
        if guess[0] == '-' and guess[1:].isdigit():
            print('Too low!')
            continue
        if not guess.isdigit():
            print("That's not a number.")
            continue
        if int(guess) > nb:
            print('Too high!')
        elif int(guess) < nb:
            print('Too low!')
        elif int(guess) == nb:
            win = True
    if win:
        if nb == 42:
            p1 = "The answer to the ultimate question of life,"
            p2 = "the universe and everything is 42."
            print(p1, p2)
        if c == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print(f"Congratulations, you've got it!\nYou won in {c} attempts!")


if __name__ == '__main__':
    main()
