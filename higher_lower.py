# import random module so as to make the number being guessed randomised

import random

# this list is responsible for the input, the number that is being guessed

guesses = []

for i in range(5):
    guesses.append(0)


# message function


def message(display):
    print(display)
    print("")


# this is the number being guessed, with guesses[2] and guesses[3] being the boundaries that the number being randomised within


guesses[2] = 1
guesses[3] = 10
guesses[4] = random.randint(guesses[2], guesses[3])

message("The correct answer is {}".format(guesses[4]))


# this is the program running and reiterating until the user has input the correct number


while True:
    try:
        guesses[1] += 1
        guesses[0] = int(input("Guess any number whole between {} and {}".format(guesses[2], guesses[3])))
        print("")
        if guesses[0] != guesses[4]:
            if guesses[0] < guesses[4]:
                message("That guess was too low")
            else:
                message("That guess was too high")
        else:
            break
    except ValueError:
        message("Error, enter any whole number between {} and {}".format(guesses[2], guesses[3]))


# this displays the output of the program


print("Good job, the answer was {}. You guessed it {} try/ies".format(guesses[4], guesses[1]))
