# variables are defined

pizza_slices = ""
people_sharing = ""

#

while not pizza_slices.isdigit():
    try:
        pizza_slices = int(input("How many slices of pizza?"))
        print("")
    except ValueError:
        print("")
        print("You must enter a whole number")

#

while not people_sharing.isdigit():
    try:
        people_sharing = int(input("How many people are sharing the pizza?"))
        print("")
    except ValueError:
        print("You must enter a whole number")
        print("")
#

print("There'll be {} slices each per person".format(pizza_slices//people_sharing))

print("There'll be {} slices remaining".format(pizza_slices % people_sharing))
