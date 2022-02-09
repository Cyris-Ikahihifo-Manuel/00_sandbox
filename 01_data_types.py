def question(answer, question, condition):
    while True:
        try:
            answer = print(question)
            print("")
        except ValueError:
            print(error)
            print("")
