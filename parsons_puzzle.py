stored_password = "Fish4321"

for i in range(10):
    password = input("Enter password:")
    if password == stored_password:
        print("Access granted")
        break
    else:
        print("Access denied")
