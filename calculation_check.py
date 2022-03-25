# addition function that makes it so that parameters a and b are added together


def add(a, b):
    text("{} + {} = {}".format(a, b, a + b))
    return True


# subtraction function that makes it so that parameters a is subtracted by parameter b


def subtract(a, b):
    text("{} - {} = {}".format(a, b, a - b))
    return True


# multiplication function that makes it so that parameter a is multiplied by parameter b

def multiply(a, b):
    text("{} x {} = {}".format(a, b, a * b))
    return True

# division function that divides parameter a by parameter b


def divide(a, b):
    text("{} / {} = {}".format(a, b, a / b))
    return True

# number function that asks users for input and will reiterate itself until the user has input a valid number


def number(message):
    while True:
        try:
            print("")
            answer = int(input(message))
            return answer
        except ValueError:
            print("")
            print("Error, enter a whole number")


# message function that adds spaces between messages


def text(message):
    print("")
    print(message)


# calculated variable is false so that the variable isn't undefined which will be used for a while loop later on

calculated = False

# program running


text("Welcome to Calculation Check")


# will forever reiterate itself as expected and also the two variables num1 and num2 are input using the number function
# that'll forever reiterate itself until has input a whole number of any value. after inputting values for variables num1
# and num2 there is another while loop that'll reiterate itself until the user has followed the instructions within
# the input's brackets (enter either +, -, * or /) the math functions return the value true which the calculated
# variable stores and ends the while loop of asking for what type of output the user would like to see

while True:
    num1 = number("Enter a whole number of any value")
    num2 = number("Enter another whole number of any value")
    while True:
        print("")
        response = input("Would you like to add (+), subtract (-), multiply (*) or divide (/)").lower().strip()
        if response == "+":
            calculated = add(num1, num2)
        elif response == "-":
            calculated = subtract(num1, num2)
        elif response == "*":
            calculated = multiply(num1, num2)
        elif response == "/":
            calculated = divide(num1, num2)
        else:
            text("Error enter either +, -, * or /")
        if calculated:
            calculated = False
            break
