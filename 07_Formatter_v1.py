"""" Component 5 Statement Formatter v1
"""

symbol = "*"
text = "Hello World"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
