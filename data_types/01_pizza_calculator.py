# this list will count as the questions, the cost and the voucher code


pizzas = []


# this creates the items in the list


for i in range(5):
    pizzas.append("")
pizzas.append(0)


# error function (i got too lazy for the pizza question functions)


def error(message):
    print("Error, {}".format(message))
    print("")


# program running


while True:
    pizzas[0] = input("Would you like thin or thick crust?").lower().strip()
    print("")
    if pizzas[0] == "thin":
        pizzas[5] += 8
        break
    elif pizzas[0] == "thick":
        pizzas[5] += 10
        break
    else:
        error("would you like either thin or thick crust")


while True:
    try:
        pizzas[1] = int(input("Pick a pizza size from 8, 10, 12, 14 or 18 inches"))
        print("")
        if pizzas[1] == 8 or pizzas[1] == 10:
            break
        elif pizzas[1] == 12 or pizzas[1] == 14 or pizzas[1] == 18:
            pizzas[5] += 2
            break
        else:
            error("pick a size from 8, 10, 12, 14 or 18 inches")
    except ValueError:
        error("pick a size from 8, 10, 12, 14 or 18 inches")


while True:
    try:
        pizzas[2] = input("Would you like cheese with your pizza? Y/N").lower().strip()
        print("")
        if pizzas[2] == "yes" or pizzas[2] == "y":
            pizzas[2] = "cheese"
            break
        elif pizzas[2] == "no" or pizzas[2] == "n":
            pizzas[2] = "no cheese"
            pizzas[5] -= 0.5
            break
        else:
            error("enter either Y or N")
    except ValueError:
        error("enter either Y or N")


while True:
    try:
        pizzas[3] = input("Which pizza type would you like? Margherita, Vegetable, Vegan, Hawaiian or Meat Feast")\
            .lower().strip()
        print("")
        if pizzas[3] == "vegetable" or pizzas[3] == "vegan":
            pizzas[5] += 1
            break
        elif pizzas[3] == "hawaiian" or pizzas[3] == "meat feast":
            pizzas[5] += 2
            break
        else:
            error("enter either Margherita, Vegetable, Vegan, Hawaiian or Meat Feast")
    except ValueError:
        error("enter either Margherita, Vegetable, Vegan, Hawaiian or Meat Feast")


while not pizzas[4] == "FunFriday" or pizzas[4] == "":
    pizzas[4] = input("If you have a voucher code, enter it now. Press enter to skip").strip()
    print("")

if pizzas[4] == "FunFriday":
    pizzas[5] -= 2

print("Your {} crust {} inch {} pizza with {} will cost ${}".format(pizzas[0], pizzas[1], pizzas[3], pizzas[2], pizzas[5]))

