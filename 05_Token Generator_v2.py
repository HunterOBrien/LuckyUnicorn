"""" component 3 (Token Generator) v2
    calculates user balance based on a random selection of tokens
"""

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]
balance = 100

# Testing loop
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t') # Wraps output making it easier to screenshot
    # Adjust the balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    elif token == "horse" or tokens == "zebra":
        balance -= 0.50

    # Output
    print(f"Token: {token}, Balance: ${balance}")
