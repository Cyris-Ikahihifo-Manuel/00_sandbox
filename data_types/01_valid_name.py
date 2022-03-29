# a while loop that reiterates until the user doesn't leave the answer as blank

name = ""

while name == "":
    name = input("Enter a name:").title().strip()
    print()
    if name == "":
        print("Name cannot be left blank")
        print()

print("Stored name: {}".format(name))
