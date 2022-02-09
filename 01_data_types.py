def question(answer, question, condition):
    while True:
        try:
            answer = question
            if condition:
                return answer
            print("")
        except ValueError:
            print(error)
            print("")
