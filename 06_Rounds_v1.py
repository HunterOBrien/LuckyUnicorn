""" Component 4 - Game Mechanics and looping v1
Based on 05_Token Generator_v4 but hard-wired to only allocate donkeys
Gives user feedback about number of rounds and maintains balance.
Test amount set to $5
"""

import random

# Main Routine
TEST_AMOUNT = 5
balance = TEST_AMOUNT

rounds_played = 0
play_again = ""

# Testing Loop to generate 5 tokens
while play_again != "x":
    rounds_played += 1  # Keep track of rounds
    number = random.randint(10, 46)  # Can only be a donkey

    # Adjust Balance
    # If the random balance is between 1 - 9
    # User gets a unicorn (Add $4 to the balance)
    if 1 <= number <= 9:
        token = "unicorn"
        balance += 4


    elif 10 <= number <= 46:
        token = "donkey"
        balance -= 1

    #  In all other cases the token must be a horse or zebra
    # Subtract $0.5 from the users balance
    else:
        # if even the token is a zebra
        if number % 2 == 0:
            token = "zebra"
            balance -= 0.5

        # Otherwise, set the token to horse
        else:
            token = "horse"
            balance -= 0.5

    # Output
    print(f"Round {rounds_played}. Token: {token}, Balance: ${balance:.2f}")
    if balance < 1:
        print("\nSorry but you have run out of money")
        play_again = "x"
    else:
        play_again = input("\nDo you want to play another round?\n<enter> to play again or 'x' to exit ").lower()

    print()

print("Thanks for playing")
print(f"You started with ${TEST_AMOUNT:.2f}")
print(f"and left with {balance:.2f}")
print("Goodbye")
