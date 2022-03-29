# defining the int_check function which reiterates itself until the user has input a whole number, displays a message
# based on the input, exits the loop and returns the value


def int_check(question):
	while True:
		try:
			response = int(input(question))
			if response < 0:
				print("What?")
			elif 1 <= response <= 5:
				print("You are too young to to de doing this yourself")
			elif 6 <= response <= 64:
				print("An okay age")
			else:
				print("Wow you're old")
			break
		except ValueError:
			print("Not a valid age")
	return response


# using a for loop to test all data types for my int_check function to see if it would run as expected or if there are
# any bugs


for i in range(4):
	int_check("How old are you?")
