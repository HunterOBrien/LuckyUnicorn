""" Component 2 (How much) v1
Ask user if they want to play and check that the input is a valid
integer between 1 and 10. If it is then this amount becomes their account balance.
"""

user_balance = int(input("Enter in a whole number between 1 and 10 to be the amount of $ you want to play with: "))

while not 1 <= user_balance <= 10:
    print("Try again, Enter in a whole number between 1 and 10")
    # Ask for input
    user_balance = int(input("How much $ do you want to play with: "))

print(f"You are playing with ${user_balance}")
