# import random module so as to make the number being guessed randomised

import random

# this list is responsible for the input, the number that is being guessed

guesses = []

for i in range(5):
    guesses.append(0)

# this is the number being guessed

guesses[4] = random.randint(guesses[2], guesses[3])

while guesses[1] < 3 or guesses[0] == guesses[4]:
    try:
        guesses[0] = int(input("Guess a number between {} and {}".format(guesses[2], guesses[3])))
        guesses[1] += 1
        print("")
    except ValueError:
        print("Enter a whole number between {} and {}".format(guesses[2], guesses[3]))
        print("")

if guesses[0] == guesses[4]:
    print("Good job, the answer was ", guesses[4])
    print("")
else:
    print("Sorry, but the correct answer was ", guesses[4])
    print("")
