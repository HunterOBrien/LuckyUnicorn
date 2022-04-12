"""" Component 5 Statement Formatter v3
    Call function three times for tests
"""


# Function to format text object
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f" {top_bottom}\n {formatted_text}\n {top_bottom}"


# Main Routine
print(formatter("-", "Welcome To Lucky Unicorn"))
print()
print(formatter("!", "Congratulations, You Got A Unicorn"))
print()
print(formatter("*", "Goodbye"))
