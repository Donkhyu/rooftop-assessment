# Function that takes an int array to find the second largest number in that array.
def getSecondLargest(int_array):
    # If length of array is less than 2, return None.
    if len(int_array) < 2:
        return None
    else:
        # Setting largest number as the max of the first two elements of the array.
        # Setting second largest number as the minimum of the first two elements of the array.
        largest_num = max(int_array[0], int_array[1])
        second_largest_num = min(int_array[0], int_array[1])

        # For loop which compares the third element of the array onwards with the values set earlier.
        for i in int_array[2:]:
            # If current number is larger than the largest number, 
            # change value of second largest number to the current value of largest number.
            # Then, change value of the largest number to the value of the current number, i.
            if i > largest_num:
                second_largest_num = largest_num
                largest_num = i
            # Else if i is larger than the second largest number but is not the largest number then, 
            # change value of the second largest number to the current number, i.
            elif i > second_largest_num and i != largest_num:
                second_largest_num = i
    
    # Return second largest number.
    return second_largest_num

# Print function call.
print(getSecondLargest([5, 4]))