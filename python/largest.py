def find_largest_number(numbers):
    # Check if the list is empty and return None
    if not numbers:
        return None

    # Initialize the largest number as the first element of the list
    largest = numbers[0]

    # Loop through the rest of the elements to find the largest
    for num in numbers[1:]:
        if num > largest:
            largest = num

    return largest

# Example usage:
sample_list = [3, 45, 12, 89, 67, 21]
result = find_largest_number(sample_list)
print(f"The largest number in the list is: {result}")