# Function that takes two integers, x and y.
# Computes division of x by y.
def divMod(x, y):
    # Intialise division count.
    div_count = 0

    # While loop to check subtraction of x - y is more than or equal to 0.
    while x - y >= 0:
        x = x - y
        # Increment division count.
        div_count += 1
    
    # Return both value of division count and x as the remainder.
    return div_count, x

# Print function call.
print(divMod(100, 7))