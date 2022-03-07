# message function


def text(message):
    print(message)
    print("")


# times table has to be defined at the very least


score = max_value = times_table = 0


# times tables number should be able to accept floats and integers but deny strings
# it should also loop forever


text("Welcome to the times tables quiz")

while True:
    try:
        times_table = float(input("What number's times table would you like to test yourself on?"))
        print("")
        while max_value <= 1:
            try:
                max_value = int(input("What's the highest whole number you would like to go try yourself on?"))
                print("")
                if max_value <= 1:
                    text("Error, enter a whole number greater than 1")
            except ValueError:
                text("Enter a whole number")
        text("Here is the {:.2f} times table up to {}".format(times_table, max_value))
        for i in range(1, max_value + 1):
            while True:
                try:
                    answer = float(input("{}. {} x {} = ?".format(i, i, times_table)))
                    if answer == i * times_table:
                        text("correct!")
                        score += 1
                    else:
                        text("sorry, but the answer was {:.2f}".format(i * times_table))
                    break
                except ValueError:
                    text("Error, enter a number")
            i += 1
        text("You got {} out of {} on the {} times tables up to {}".format(score, max_value, times_table, max_value))
        score = 0
        max_value = times_table = 0
        print("")
    except ValueError:
        text("Error, enter a whole number")
