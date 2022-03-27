""" Component 2 (How much) v2
uses a try except and pull error message out of the loop
"""

error = "Please enter a whole number between 1 and 10\n"
valid = False

while not valid:
    try:
        # Ask for amount
        user_balance = int(input("How much would you like to play with? $"))

        if 0 < user_balance <= 10:
            print(f"You are playing with {user_balance}")
            valid = True
        else:
            print(error)

    except ValueError:
        print(error)
