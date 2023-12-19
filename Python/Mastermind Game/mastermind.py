import random

MAX_GUESSES = 10
MAX_COLORS = 4
choices = ["R", "G", "B", "W", "O", "Y"]


def generate_colors():
    colors_list = []

    for i in range(MAX_COLORS):
        color = random.choice(choices)
        colors_list.append(color)

    return colors_list


def guess_input():
    while True:
        guess = input("Guess the 4 colors (space separated): ").upper().split(" ")

        if len(guess) != MAX_COLORS:
            print(f"You have to guess {MAX_COLORS} colors")
            continue

        for x in guess:
            if x not in choices:
                print(f"{x} is not a valid color")
                print(f"Valid colors are: ", *choices)
                break
        else:
            break

    return guess


def check_guess(guess, colors):
    correct_positions = 0
    incorrect_positions = 0
    colors_2 = colors.copy()
    guess_2 = guess.copy()

    for i in range(len(colors)):
        if guess[i] == colors[i]:
            correct_positions += 1
            colors_2.remove(guess[i])
            guess_2.remove(guess[i])

    while len(guess_2) > 0:
        if guess_2[0] in colors_2:
            incorrect_positions += 1
            guess_2.remove(guess_2[0])
        else:
            guess_2.remove(guess_2[0])

    return correct_positions, incorrect_positions


def game():
    tries = 0
    colors = generate_colors()
    print(colors)
    while tries < 10:
        guess = guess_input()
        cor_pos, incor_pos = check_guess(guess, colors)

        tries += 1

        if cor_pos == MAX_COLORS:
            print(f"You guess it in {tries} tries!")
            break

        print(f"Correct positions: {cor_pos} | Incorrect positions: {incor_pos}")


game()






