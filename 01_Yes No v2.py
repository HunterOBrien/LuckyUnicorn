""" LU Yes No checker V2
Checks whether the user has played lucky unicorns before and also show the user what they entered
"""

# Ask the user if they have played before (We simplify it useing .upper() to reduce possible combination for yes/no
show_instructions = input("Have you played this game before? : ").upper()
# If they say yes, output: program continues
if show_instructions == "YES" or show_instructions == "Y":
    print("Program continues")
# If they say no, output: display instructions
elif show_instructions == "NO" or show_instructions == "N":
    print("Give instructions")
# otherwise, show error
else:
    print("Please answer yes or no")

print(f"You entered '{show_instructions}'")
