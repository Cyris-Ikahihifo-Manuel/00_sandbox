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


# data types program running

questions = [data_types(input("What's your name?").strip(), "", "You must enter something other than pressing enter key"),
             data_types(int(input("How old are you?")), "", "You must enter your age in numbers"),
             data_types(input("What's your favorite animal?").strip(), "", "You must enter something other than pressing enter key"),
             data_types(float(input("What are the first four digits of PI?")), "", "The answer is a number followed by decimals")]
