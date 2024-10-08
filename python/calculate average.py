def calculate_average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

# Testing the function with different numbers of arguments
print(calculate_average(10, 20, 30))        # Output: 20.0
print(calculate_average(5, 15))             # Output: 10.0
print(calculate_average(7))                 # Output: 7.0
print(calculate_average())                  # Output: 0
print(calculate_average(4, 8, 12, 16, 20))  # Output: 12.0