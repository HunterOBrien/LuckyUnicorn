""" Component 2 (How much) v4
Turned the component into a function and added more ability for the code to be recycled
"""


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


# Main routine
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with {user_balance}")
