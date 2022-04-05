""" component 3 (Token Generator) v3
    changes the odds of the different tokens appearing in order to favor the house.

"""

import random

tokens = ["unicorn", "horse", "horse", "horse", "donkey", "donkey",
          "donkey", "donkey", "zebra", "zebra", "zebra"]
balance = 100

# Testing loop
for item in range(100):
    token = random.choice(tokens)
    print(token, end='\t')  # Wraps output making it easier to screenshot
    # Adjust the balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    elif token == "horse" or tokens == "zebra":
        balance -= 0.50

    # Output
    print(f"Token: {token}, Balance: ${balance}")
