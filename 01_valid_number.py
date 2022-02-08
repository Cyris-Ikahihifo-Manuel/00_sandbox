# a while loop that reiterates itself until the user has input a whole number between 1 and 10

number = 0

while not 1 <= number <= 10:
    try:
        number = int(input("Enter a whole number between 1 and 10:"))
        if 1 <= number <= 10:
            print(number)
        else:
            print("Number out of range")
    except ValueError:
        print("You must enter a whole number between 1 and 10")

