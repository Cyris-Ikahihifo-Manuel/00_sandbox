# the variable is name, its input with a .lower() which should convert uppercase letters into lowercase. if the input
# is anakin or leia their output is unique. there are no parameters so any data type (float, integer or string) should
# work too

name = input("What is your name?").lower()

if name == "anakin":
    print("How do you do Anakin!")
elif name == "leia":
    print("The force is with you")
else:
    print("Nice name, {}.".format(name))

# the variable is weather, its input with a .upper() which should convert lowercase letters into uppercase. if the input
# is hot or cold their output is unique. there are no parameters so any data type (float, integer or string) should
# work too

weather = input("So {}, is it hot or cold where you are today?".format(name)).upper()
if weather == "COLD":
    print("You must be freezing!")
elif weather == "HOT":
    print("Drink plenty of water")
else:
    print("I can't advise you on that type of weather.")

# the variable is likes_blue, its input with a .upper() which should convert lowercase letters into uppercase. if the input
# is yes the output is unique. there are no parameters so any data type (float, integer or string) should work too

likes_blue = input("Do you like the colour blue?").upper()
if likes_blue == "YES":
    print("I like blue too")
else:
    print("That’s a shame because I really like blue")

print("Have a good day! Bye!")
