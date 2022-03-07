# The sandwich_list is a list that is responsible for the input and the total cost (output) because of the user's
# input

sandwich_list = []

for i in range(6):
    sandwich_list.append("")
sandwich_list.append(0)


# sandwich order function one when there's only two decisions


def order(response, question, ans1, ans2):
    while True:
        if response != ans1 or response != ans2:
            response = input(question).lower().strip()
        else:
            return response


# sandwich order for when there are three options


def order2(response, question, ans1, ans2, ans3):
    while True:
        if response != ans1 or response != ans2 or response != ans3:
            response = input(question).lower().strip()
        else:
            return response


# This asks the user what their meal is (asks the user for an input) the while statements are there to be as parameters
# and are also there to reiterate until the user has input something within the parameters


while True:
    if sandwich_list[0] != "sandwich" or sandwich_list[0] != "wrap":
        sandwich_list[0] = input("Sandwich or Wrap?").lower().strip()
    else:
        break


while True:
    if sandwich_list[1] != "meat" or sandwich_list[1] != "vegetarian" or sandwich_list[1] != "vegan":
        sandwich_list[1] = input("Meat, Vegetarian or Vegan?").lower().strip()
    else:
        break


while True:
    if sandwich_list[4] != "yes" or sandwich_list[4] != "no" or sandwich_list[4] != "y" or sandwich_list[4] != "n":
        sandwich_list[4] = input("Would you like it with extra sauce? Y/N").lower().strip()
    else:
        break


while True:
    if sandwich_list[2] != "cookies" or sandwich_list[2] != "chips" or sandwich_list[2] != "fruit" or sandwich_list[2] != "none":
        sandwich_list[2] = input("Cookies, Chips, Fruit or None?").lower().strip()
    else:
        break


while True:
    if sandwich_list[3] != "fizzy drink" or sandwich_list[3] != "water" or sandwich_list[3] != "juice" or sandwich_list[3] != "none":
        sandwich_list[3] = input("Fizzy drink, Water, Juice or None?").lower().strip()
    else:
        break


while True:
    if sandwich_list[5] != "yes" or sandwich_list[4] != "no" or sandwich_list[5] != "y" or sandwich_list[5] != "n":
        sandwich_list[5] = input("Would you like it with extra salad? Y/N").lower().strip()
    else:
        break


# This calculates the cost of the order (this is the output)


if sandwich_list[0] == "sandwich":
    sandwich_list[6] += 2
else:
    sandwich_list[6] += 3

if sandwich_list[1] == "vegetarian" or sandwich_list[1] == "vegan":
    sandwich_list[6] += 1
else:
    sandwich_list[6] += 1.5

if sandwich_list[2] == "cookie" and sandwich_list[3] == "fizzy drink":
    sandwich_list[6] += 0.5
else:
    sandwich_list[6] -= 0.5

if sandwich_list[4] == "yes" or sandwich_list[4] == "y" and sandwich_list[5] == "yes" and sandwich_list[5] == "y":
    sandwich_list[6] += 1


# This prints the output


print("That'll cost ${} Enjoy your meal!".format(sandwich_list[6]))
