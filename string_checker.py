# defining the int_check function which reiterates itself until the user has input a whole number, displays a message
# based on the input, exits the loop and returns the value


def int_check(question):
    while True:
        response = input(question)
        num_check = check_input(response)
        if num_check:
            if 1 <= int(response) <= 5:
                print("")
                print("You are too young to to de doing this yourself")
            elif 6 <= int(response) <= 64:
                print("")
                print("An okay age")
            else:
                print("")
                print("Wow you're old")
            return response


# ask_name function which reiterates itself until the user has input a string.


def ask_name(question):
    while True:
        print("")
        answer = input(question).lower().title().strip()
        named = check_input(answer)
        if named:
            return answer


# defining the str_check function which reiterates itself until the user has input a string, displays an error message
# if the user has input a digit (- and . are interpreted as a dash and full stop and so should be interpreted as
# strings)


def check_input(response):
    if response.isdigit():
        print("")
        print("Error, this value isn't a number")
    else:
        return response.isdigit()


# calling the functions and testing all values


for i in range(4):
    age = int_check("How old are you?")
    name = ask_name("What's your name?")


# message is displayed that uses the input of variables age and name


print("")
print("Oh so you're {} years old, {}? Huh?".format(age, name))
