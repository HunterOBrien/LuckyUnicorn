"""" component 3 (Token Generator) v1
    Generates random token,in a random order
"""

import random

tokens = ["unicorn", "horse", "donkey", "zebra"]

# Testing loop
for item in range(20):
    token = random.choice(tokens)
    print(token, end='\t') # Wraps output making it easier to screenshot
