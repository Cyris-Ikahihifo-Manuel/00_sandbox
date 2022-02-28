# question function


def question(message):
    while True:
        guess = input("{} Y/N".format(message)).strip().lower()
        print("")
        if guess == "yes" or guess == "y":
            guess = "yes"
            return guess
        elif guess == "no" or guess == "n":
            guess = "no"
            return guess
        else:
            print("Error, please enter either 'yes' or 'no'")
            print("")


# text function


def text(message):
    print(message)
    print("")


# program running

print("""Pick either Carrot, Broccoli, Peas or Sweetcorn
I will attempt to guess your choice""")
print("")

answer = question("Is your vegetable green?")

if answer == "yes":
    answer = question("Does the vegetable look like a tree?")
    if answer == "yes":
        text("It must be Peas!")
    else:
        text("It must be Broccoli!")
else:
   answer = question("Is your vegetable orange?")
   if answer == "yes":
       text("It must be a Carrot!")
   else:
       text("It must be Sweetcorn!")
