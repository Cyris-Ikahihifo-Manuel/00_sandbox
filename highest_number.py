# highest function that compares two parameters a and b (amount of numbers) and which parameter is
# higher than the other

def highest(a, b):
    if a > b:
        highest_num = a
    else:
        highest_num = b
    print("The highest number entered is {}".format(highest_num))


# number function that reiterates itself until the user has input a number


def num(message):
    while True:
        try:
            print("")
            response = int(input(message))
            return response
        except ValueError:
            print("")
            print("Error, enter a whole number of any value")


# program running


num1 = num("Enter a whole number of any value")
num2 = num("Enter another whole number of any value")


# highest function takes the input of variables num1 and num2, compares the two variables and which is the
# higher value displays the output

highest(num1, num2)
