""" LU base component
components added after they have been created and tested
"""


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
    print("The Rules Of The Game Go Here")
    print()
    print("Program Continues")
    print()


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


# Main routine goes here
# Checks whether the user needs instructions
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()

# Asks how much the user wants to play with
user_balance = num_check("How much would you like to play with $", 1, 10)
print(f"You are playing with {user_balance}")
