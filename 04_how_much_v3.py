""" Component 2 (How much) v3
compressed the code into something more efficient
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
