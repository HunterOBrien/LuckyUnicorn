"""" LU Yes No checker v3
Checks whether the user has played lucky unicorns before
and putting the code inside a loop until the user enters a correct answer
"""


# Creates variable show instructions
show_instructions = ""

# Puts show instructions inside a loop until the user enters a correct answer
while show_instructions != "x":
    # Ask the user if they have played before (We simplify it using .upper() to reduce possible combination for yes/no
    show_instructions = input("Have you played this game before? : ").lower()
    # If they say yes, output: program continues
    if show_instructions == "yes" or show_instructions == "y":
        print("Program continues")

    # If they say no, output: display instructions
    elif show_instructions == "no" or show_instructions == "n":
        print("Give instructions")

    # otherwise, show error
    else:
        print("Please answer yes or no")

    print(f"You entered '{show_instructions}'")
