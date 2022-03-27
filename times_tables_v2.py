# question function which asks the user


def question(message, error_message):
    while True:
        try:
            response = message
            print("")
            return response
        except ValueError:
            text(error_message)


# times tables function which uses a for loop and reiterates until the i is equal to the max value + 1 since the for
# loop seems to end at a value just one increment less than the max value (not parameter max_value)


def times_tables(max_value):
    if max_value >= 1:
        text("Here is the {:.2f} times table up to {}".format(times_table, max_value))
        for i in range(1, max_value + 1):
            print("{}. {} x {} = {:.2f}".format(i, i, times_table, i * times_table))
        print()
    else:
        text("Here is the {:.2f} times table down to {}".format(times_table, max_value))
        for i in range(1, max_value - 1):
            print("{}. {} x {} = {:.2f}".format(i, i, times_table, i * times_table))
        print()




# message function


def text(message):
    print(message)
    print("")


# times table has to be defined at the very least


max_value = times_table = 0


# times tables number should be able to accept floats and integers but deny strings
# it should also loop forever


while True:
    question(float(input("Enter a number of any value to see it being multiplied")), "Error, enter a number of any value")
    question(int(input("Whats the highest whole number you'd like to see the number being multiplied by?")), "Error, enter a whole number")
