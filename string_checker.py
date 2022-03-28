# defining the int_check function which reiterates itself until the user has input a number, if the input is a
# "negative" number or the number is a "float" the function displays an error message that says to enter a positive
# whole number of any value


def int_check(question):
    while True:
        response = input(question)
        if response.isdigit():
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
        else:
            print("")
            print("Error, enter a positive whole number of any value")


# ask_name function which reiterates itself until the user has input a string. If the user has input a "float" or
# "negative" number the isdigit() should interpret them as a dash and a full stop and so would be classed as strings


def ask_name(question):
    while True:
        print("")
        answer = input(question).title().strip()
        number = check_input(answer)
        if number == False:
            return answer


# defining the check_input function which outputs a message if the parameter 'response' is a whole number.
# It will only return the parameter response's boolean if the parameter response is a string (so it will only return
# the value False). And also if the user has input a digit (- and . are interpreted as a dash and full stop and so
# should be interpreted as strings)


def check_input(response):
    if response.isdigit():
        print("")
        print("Error, this value is a number")
    else:
        return response.isdigit()


age = name = 0


# calling the functions and testing all values

for i in range(3):
    age = int_check("How old are you?")
name = ask_name("What's your name?")


# message is displayed that uses the input of variables age and name


print("")
print("Oh so you're {} years old, {}?".format(age, name))
