# Initialise stack as an empty array.
stack = []

# Append array acts as push operation to a stack.
stack.append(1)
stack.append(2)
stack.append(3)
print("Current stack:", stack)

# Pop array acts as pop operation to a stack.
stack.pop()
print("Current stack:", stack)

# Checking the last element of the array acts as peek operation to a stack.
print("Peeking stack:", stack[-1])