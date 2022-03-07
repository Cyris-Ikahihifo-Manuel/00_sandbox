# average value function that adds the three parameters together and divides them by the score (amount of numbers) there
# were within the brackets

def average_value(a, b, c):
    print("the average is {:.2f}".format((a+b+c)/3))


# number function that asks the user for their input


def num():
    while True:
        try:
            response = float(input("Enter a number of any value"))
            print("")
            return response
        except ValueError:
            print("Error, enter a number of any value")
            print("")

# number list that'll serve as a variable also for later


number = []
for i in range(3):
    number.append(0)


# user is asked for input of a number for a number of any value which will be used for later


for i in range(len(number)):
    number[i] = num()


# input previously is now displayed as output as the average of the three inputs

average_value(number[0], number[1], number[2])
