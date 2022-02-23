# import random module so as to make the number being guessed randomised

import random

# this list is responsible for the input, the number that is being guessed

guesses = []

for i in range(5):
    guesses.append(0)

def num_Q(question, condition):
    while True:
        try:
            variable = question
            print("")
            if variable > condition:
                return variable
        except ValueError:
            print("Error, enter a positive whole number")
            print("")


# this is the number being guessed, with guesses[2] and guesses[3] being the boundaries that the number being randomised within


num_Q(int(input("Enter any positive whole number")), 1)


while True:
    try:
        guesses[3] = int(input("Enter a positive whole number greater than ", guesses[2]))
        print("")
        if guesses[3] > guesses[2]:
            break
    except ValueError:
        print("Error, enter a positive whole number")
        print("")


guesses[4] = random.randint(guesses[2], guesses[3])

print("The answer is ", guesses[4])
print("")


# this is the program running and reiterating until the user has input that is guesses[4] or they've input 3 times


while True:
    try:
        guesses[0] = int(input("Guess any number between {} and {}".format(guesses[2], guesses[3])))
        print("")
        guesses[1] += 1
        if guesses[0] < guesses[2] or guesses[0] > guesses[3]:
            print("Number out of range, enter a whole number between {} and {}".format(guesses[2], guesses[3]))
            print("")
        if guesses[1] == 3 or guesses[0] == guesses[4]:
            break
    except ValueError:
        print("Error, enter a positive whole number")
        print("")


# this displays the output of the program


if guesses[0] == guesses[4]:
    print("Good job, the answer was ", guesses[4], "you did in ", guesses[1], " attempt/s")
    print("")
else:
    print("Sorry, but the correct answer was ", guesses[4])
    print("")
