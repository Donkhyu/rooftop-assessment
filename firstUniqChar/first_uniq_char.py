# Function which takes in a string.
def firstUniqChar(string):
    # Initialize the order and count as an empty array and dict respectively.
    order = []
    counts = {}

    # For loop to go through each letter in the string.
    for l in string:
        # If letter is found in counts, increment the count of letter by 1.
        if l in counts:
            counts[l] += 1
        # Else, set the count of letter to 1 and append the letter to the order array.
        else:
            counts[l] = 1
            order.append(l)
    
    # For loop to check through each letter in order dict.
    for l in order:
        # If the count of a letter is 1, return the letter.
        if counts[l] == 1:
            return l
        
    # Return None if no unique characters are found.
    return None

# Print function call.
print(firstUniqChar("parallel"))