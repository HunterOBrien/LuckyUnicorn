""" Component 4 - Game Mechanics and looping v3
Based on 06_Rounds_v2 but the code is now in a function
"""

import random


# Function To generate random token
def generate_token(balance):
    rounds_played = 0
    play_again = ""

    # Testing loop to generate 5 tokens
    while play_again != "x":
        rounds_played += 1  # Keeps track of rounds
        number = random.randint(1, 100)  # Generates Token

        # Adjust Balance
        # If the random balance is between 1 - 9
        # User gets a unicorn (Add $4 to the balance)
        if 1 <= number <= 9:
            token = "unicorn"
            balance += 4

        # If the random number is between 10 and 46
        # The user gets a Donkey (Minus $1)

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
            play_again = input("\nDo you want to play another round?\n<enter> to "
                               "play again or 'x' to exit ").lower()

        print()
    return balance


# Main Routine
starting_balance = 5
closing_balance = generate_token(starting_balance)

print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and left with {closing_balance:.2f}")
print("Goodbye")
