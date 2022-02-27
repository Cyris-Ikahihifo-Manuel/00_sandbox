# message function


def text(message):
    print(message)
    print("")


# times tables number should be able to accept floats and integers but deny strings it should also be able to loop

while True:
    try:
        times_table = float(input("What number's times table would you like to see up to 12 enter 'd' if you're finished with the times table"))
        print("")
        text("Please enter a number")
        for i in range(1, 12):
            print("{}. {} x {} = {}".format(i, i, times_table, i * times_table))
            i += 1
    except ValueError:
        if times_table != "d":
            text("Please enter a number")
        else:
            break


# Program finishes


text("Goodbye user")
