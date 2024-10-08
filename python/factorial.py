def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


def get_non_negative_integer():
    while True:
        try:
            user_input = int(input("Enter a non-negative integer: "))
            if user_input < 0:
                print("Please enter a non-negative integer.")
            else:
                return user_input
        except ValueError:2
            print("Invalid input. Please enter a non-negative integer.")


number = get_non_negative_integer()
result = factorial(number)
print(f"The factorial of {number} is: {result}")