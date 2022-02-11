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

response = ["", ""]

questions = [data_types(input("What's your name?").strip(), "", "You must enter something other than pressing enter key"),
             data_types(input("What's your favorite animal?").strip(), "", "You must enter something other than pressing enter key")]

while True:
    try:
        response[1] = int(input())
        print("")
        if response[1] >= 0:
            return response
        else:
            print("You must enter a valid age")
            print("")
    except ValueError:
        print("You must enter a valid age")
        print("")
