""" component 3 (Token Generator) v4
    Calculates percentages to ensure odds are in favor of the house
    9% Unicorns, 37% Donkey, and 27% for Zebra and Horse
"""

import random

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# Testing loop
for item in range(100):
    number = random.randint(1, 100)

    # Adjust balance
    # If the num is between 1 and 9 user gets unicorn (9% chance) (+ $4)
    if 1 <= number <= 9:
        token = "unicorn"
        balance += 3

    # If the num is between 10 and 46 user gets donkey (37% chance) (- $1)
    elif 10 <= number <= 46:
        token = "donkey"
        balance -= 1

    # If the num is between 47 and 73 user gets zebra (27% chance) (- $0.5)
    elif 47 <= number <= 73:
        token = "zebra"
        balance -= 0.5

    # If the num is between 74 and 100 user gets horse (27% chance) (- $0.5)
    elif 74 <= number <= 100:
        token = "horse"
        balance -= 0.5

    # Output
    print(f"Token: {token}, Balance: ${balance:.2f}")

print()
print(f"Starting Balance is equal to ${STARTING_BALANCE:.2f}")
print(f"Final Balance is equal to ${balance:.2f}")
