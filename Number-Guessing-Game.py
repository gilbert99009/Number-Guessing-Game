import random


def start_game():
    # 1. Display an intro/welcome message to the player.
    print("""
------------------------------------
Welcome to the Number Guessing Game!
------------------------------------""")

    highscore = [10]

    def inner_play(highscore):
        # 2. Store a random integer as the answer/solution. Initialization
        answer = random.randint(1, 10)
        list_of_guesses = []
        initialize = 1

        while bool(initialize) == True:
            try:
                guess = int(input("Please guess a number from 1 - 10:      "))
                if guess > 10 or guess <= 0:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number from 1 - 10!")
                continue

            list_of_guesses.append(guess)
            if guess > answer:
                print("It's lower!")
                continue
            elif guess < answer:
                print("It's higher!")
                continue
            elif guess == answer:
                print("Number of tries took:  {}!".format(len(list_of_guesses)))
                print("The winning number is {}!".format(answer))
                if len(list_of_guesses) < min(highscore):
                    highscore.append(len(list_of_guesses))
                    print("New highscore!")
                print("The highscore is {}!".format(min(highscore)))
                list_of_guesses.clear()
                break
    # initialize the inner game function
    inner_play(highscore)

    while True:
        # ask the user if he/she wants to restart the game
        restart_game = input("You got it! Would you like to play again? (Y/N)     ")
        if restart_game.lower() == "y":
            inner_play(highscore)
        if restart_game.lower() == "n":
            print("GAME ENDING!")
            break
#       else:
#         print("Please type in [Y]es/[N]o")

if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
