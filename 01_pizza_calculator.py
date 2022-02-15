# this list should count as all the options of the pizza with the final index being the total cost and the array
# should be the parameters in the code

code = 0
total_cost = 0
pizza_list = []
pizza_arrays = [["thick", "thin"], ["8", "10", "12", "14", "18"], ["yes", "no", "y", "n"],
                ["Margherita", "Vegetable", "Vegan", "Hawaiian", "Meat Feast"]]

for i in range(5):
    pizza_list.append(0)

# this function should ask a question and return the input and reiterate itself until the user has input a answer within
# the parameters


def pizza(answer, question, parameter, error):
    while False:
        try:
            answer = question
            print("")
            if answer in parameter:
                return answer
            else:
                print(error)
                print("")
        except ValueError:
            print(error)
            print("")


# running the program

pizza_list[0] = pizza(pizza_list[0], input("Would you like a thick or thin crust").lower(), pizza_arrays[0], "Error, enter either thick or thin")
if pizza_list[0] == "thick":
    total_cost += 10
else:
    total_cost += 8
pizza_list[1] = pizza(pizza_list[1], int(input("Pick a pizza size from 8, 10, 12, 14 or 18 inches")), pizza_arrays[1], "Error, enter either 8, 10, 12, 14 or 18")
if 10 < pizza_list[1] <= 18:
    total_cost += 2
pizza_list[2] = pizza(pizza_list[2], input("Would you like cheese with your pizza Y/N".lower()), pizza_arrays[2], "would you like cheese with your pizza or not")
pizza_list[3] = pizza(pizza_list[3], input("Which pizza type would you like? Margherita, Vegetable, Vegan, Hawaiian or Meat Feast")
                      .lower().title(), pizza_arrays[3], "Error, either Margherita, Vegetable, Vegan, Hawaiian or Meat Feast")
if pizza_list[3] == "Vegetable" or pizza_list[3] == "Vegan":
    total_cost += 1
elif pizza_list[3] == "Hawaiian" or pizza_list[3] == "Meat Feast":
    total_cost += 2

while code != "FunFriday" or code != "":
    code = input("""If you have a voucher code, enter it now
Press enter to skip""").strip()

if code == "FunFriday":
    total_cost -= 2
