# defining the int_check function which reiterates itself until the user has input a whole number, displays a message
# based on the input, exits the loop and returns the value


def int_check(question):
    while True:
        try:
            response = int(input(question))
            if response < 0:
                print("What?")
            elif 1 <= response <= 5:
                print("You are too young to to de doing this yourself")
            elif 6 <= response <= 64:
                print("An okay age")
            else:
                print("Wow you're old")
            break
        except ValueError:
            print("Not a valid age")
    return response


# defining the str_check function which reiterates itself until the user has input a string, displays an error message
# if the user has input a


def check_input(question):
    while True:
        response = input(question)
        if response.isdigit():
            print("Enter a string")
        else:
            return response


# calling the functions and testing all values


for i in range(4):
    age = int_check("How old are you?")
    name = check_input("What's your name?")


# message is displayed that uses the input of variables age and name


print("hello {} year old {}".format(age, name))
