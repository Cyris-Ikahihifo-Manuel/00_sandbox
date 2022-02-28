# message function


def text(message):
    print(message)
    print("")


# question function that reiterates itself until the user has input something valid
# times table has to be defined at the very least


max_value = times_table = 0


# times tables number should be able to accept floats and integers but deny strings it should also be able to loop


while True:
    try:
        times_table = float(input("What number's times table would you like to see enter 'd' if you're finished"))
        print("")
        while max_value <= 1:
            try:
                max_value = int(input("What's the highest whole number you would like to see it multiplied"))
                print("")
            except ValueError:
                text("Enter a whole number")
        text("Here is the {} times table up to {}".format(times_table, max_value))
        for i in range(1, max_value):
            print("{}. {} x {} = {:.2f}".format(i, i, times_table, i * times_table))
            i += 1
        max_value = times_table = 0
        print("")
    except ValueError:
        times_table = times_table.str()
        if times_table == "d":
            break
        else:
            print("Enter a whole number")


# Program finishes


text("Goodbye user")
