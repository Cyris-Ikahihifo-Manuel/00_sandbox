# data types function


def data_types(question, condition, error):
    while True:
        try:
            answer = question
            if condition:
                return answer
            else:
                print("")
                print(error)
            print("")
        except ValueError:
            print(error)
            print("")


# data types program running

questions = [data_types("What's your name", , )]
