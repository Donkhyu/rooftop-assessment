# Function that takes a number and counts the amount of 3s in that number.
def countDigit(number):
    # Only takes in a positive integer, else returns None.
    if number >= 0:
        # Convert number to string and return count of "3" in that string.
        number_str = str(number)
        return number_str.count("3")
    else:
        return None

# Print function call.
print(countDigit(3333))