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


def instructions():
    print("***** How To Play *****")
    print()
    print("The Rules Of The Game Go Here")
    print()
    print("Program Continues")
    print()


# Main routine goes here
played_before = yes_no("Have you played this game before? ")

if played_before == "No":
    instructions()
else:
    print("Program Continues")
