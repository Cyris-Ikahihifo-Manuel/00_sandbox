# data types function


def data_types(question, condition, error):
    while True:
        try:
            answer = question
            if answer != condition:
                return answer
            else:
                print("")
                print(error)
            print("")
        except ValueError:
            print(error)
            print("")


# age question function


def age():
    while True:
        try:
            answer = int(input("How old are you?"))
            print("")
            if answer > 0:
                return answer
            else:
                print("You must enter a valid age")
                print("")
        except ValueError:
            print("You must enter a valid age")
            print("")


# whats PIs digit function


def whats_pi():
    while True:
        try:
            answer = int(input())
            print("What are the first three decimals of pi?")
            return answer
        except ValueError:
            print("You must enter a number")
            print("")


# data types program running


questions = [data_types(input("What's your name?").strip(), "", "You must enter something other than pressing enter key"), age(),
             data_types(input("What's your favorite animal?").strip(), "", "You must enter something other than pressing enter key"),
             whats_pi()]

print(questions)
