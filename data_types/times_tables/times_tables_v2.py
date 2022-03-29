# question function is usually used for input. This will be used later as the number the user would to see being
# multiplied and how far or down (negative times tables) the user would like to see that number being multiplied


def question(message, error_message):
    while True:
        try:
            response = float(input(message))
            print("")
            return response
        except ValueError:
            text(error_message)


# times tables function which uses a for loop and reiterates until the i is equal to the max value + 1 since the for
# loop seems to end at a value just one increment less than the max value (not parameter max_value)


def times_tables(multiplied_num, max_value):
    index = 0
    if max_value >= 1:
        text("Here is the {:.2f} times table up to {}".format(multiplied_num, max_value))
        for i in range(1, max_value + 1):
            index += 1
            print("{}. {} x {} = {:.2f}".format(index, i, multiplied_num, i * multiplied_num))
        print()
    else:
        text("Here is the {:.2f} times table down to {}".format(multiplied_num, max_value))
        for i in range(1, max_value - 1, -1):
            index += 1
            print("{}. {} x {} = {:.2f}".format(index, i, multiplied_num, i * multiplied_num))
        print()


# message function which prints the parameter message and prints a blank space. This is for aesthetics and is
# unnecessary but i like it so it gets to stay


def text(message):
    print(message)
    print("")


# times table has to be defined at the very least so that they aren't considered undefined.


number = multiply_to = 0


# program running, the variables 'number' and 'multiply_to' use the question function for input which will be used in
# the times_tables function and display the output.


while True:
    number = question("Enter a number of any value to see it being multiplied", "Error, enter a number of any value")
    multiply_to = question("Whats the highest whole number you'd like to see the number being multiplied by? (Your answer will be rounded if its a decimal)", "Error, enter a whole number of any value")
    times_tables(number, round(multiply_to))
