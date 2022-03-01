# message function


def text(message):
    print(message)
    print("")


# times table has to be defined at the very least


max_value = times_table = 0


# times tables number should be able to accept floats and integers but deny strings
# it should also loop forever


while True:
    try:
        times_table = float(input("What number's times table would you like to see"))
        print("")
        while max_value <= 1:
            try:
                max_value = int(input("What's the highest whole number you would like to see it multiplied"))
                print("")
                if max_value <= 1:
                    text("enter a whole number greater than 1")
            except ValueError:
                text("Enter a whole number")
        text("Here is the {:.2f} times table up to {}".format(times_table, max_value))
        for i in range(1, max_value + 1):
            print("{}. {} x {} = {:.2f}".format(i, i, times_table, i * times_table))
            i += 1
        max_value = times_table = 0
        print("")
    except ValueError:
        text("Enter a whole number")
