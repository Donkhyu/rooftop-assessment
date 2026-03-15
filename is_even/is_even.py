# Change value of n to get different results.
n = 0

# Function that checks remainder of division of n by 2.
# If 0, return True, else, return False.
def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

# Function call.
isEven(n)