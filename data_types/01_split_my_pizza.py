# pizza question function


def pizza(question, error):
    valid = True
    while valid:
        try:
            print("")
            answer = int(input(question))
            valid = True
            return answer
        except ValueError:
            print("")
            print(error)


# this list should be both of the questions (how many slices of pizza and how many are sharing)

pizza_questions = [pizza("How many slices of pizza", "You must enter a whole number"),
                   pizza("How many people are sharing", "You must enter a whole number")]

# this should reveal how many slices each and how many slices are left over

print("There'll be {} slices each per person".format(pizza_questions[0] // pizza_questions[1]))

print("There'll be {} slices remaining".format(pizza_questions[0] % pizza_questions[1]))
