# Initialize value of i to 0.
i = 0

# While loop when i is less than 100.
while i < 100:
    # Increment i by 1.
    i += 1

    # If else statements to check if i is divisible by 3 or 5 by remainder being 0.
    # Prints "FizzBuzz" if divisible by 3 and 5.
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    # Prints "Fizz" if divisible by 3.
    elif i % 3 == 0:
        print("Fizz")
    # Prints "Buzz" if divisible by 5.
    elif i % 5 == 0:
        print("Buzz")
    # Else it just prints the number, i.
    else:
        print(i)