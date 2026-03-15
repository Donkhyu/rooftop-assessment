# Function that finds the greater of two integers x and y.
def greaterOfTwo(x, y):
# Prints the larger number.
    print(x * (x >= y) + y * (y > x))

# Change values of x and y to obtain different results.
x = 4
y = 7

# Function call.
greaterOfTwo(x, y)