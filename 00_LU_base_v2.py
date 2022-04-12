""" LU base component
components added after they have been created and tested
"""

import random


# Functions go here
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output: program continues
        if answer == "yes" or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output: display instructions
        elif answer == "no" or answer == "n":
            answer = "No"
            return answer

        # otherwise, show error
        else:
            print("Please answer yes or no")


# Function to display instructions
def instructions():
    print("***** How To Play *****")
    print()
    print("You pay $1 each round and are given a random token")
    print()
    print("This random token is either a Unicorn, Donkey, Zebra or Horse")
    print()
    print("Unicorns give you money if you get one, but the other three tokens")
    print("Make you lose money")
    print()
    print("Press enter to keep playing, or 'x' to cash out")


# Number checking function
def num_check(question, low, high):
    error = "That was not a valid input\n" \
            "Please enter a whole number between {} and {}\n".format(low, high)

    # Keep asking until a valid amount is given
    while True:
        try:
            # Ask for amount
            response = int(input(question))

            # Check for num in required range
            if low <= response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


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


# Main routine goes here

# Checks whether the user needs instructions
played_before = yes_no("Have you played this game before? ")
if played_before == "No":
    instructions()

# Asks how much the user wants to play with
starting_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with {starting_balance}")

# Generate Token
closing_balance = generate_token(starting_balance)
print("Thanks for playing")
print(f"You started with ${starting_balance:.2f}")
print(f"and left with {closing_balance:.2f}")
print("Goodbye")
