# Function that reverses the given string.
def stringReverse(string):
    # Empty string initialised.
    reversed_str = ""
    # For each character in the given string, add to the empty string and return the reversed string.
    for char in string:
        reversed_str = char + reversed_str
    return reversed_str

# Print function call.
print(stringReverse("hello"))