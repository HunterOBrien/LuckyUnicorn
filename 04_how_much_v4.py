""" Component 2 (How much) v2
uses a try except and pull error message out of the loop
"""

error = "Please enter a whole number between 1 and 10\n"
user_balance = 0

while not 1 <= user_balance <= 10:
    try:
        # Ask for amount
        user_balance = int(input("How much would you like to play with? $"))

        print()

    except ValueError:
        print(error)

print(f"You are playing with {user_balance}")
