def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_string == cleaned_string[::-1]


test_cases = [
    "A man, a plan, a canal: Panama",
    "Was it a car or a cat I saw?",
    "No lemon, no melon!",
    "Racecar",
    "Hello, World!",
    "Madam in Eden Im Adam",
    "12321",
    "Not a palindrome"
]
print("Checking for palindromes...")
for test in test_cases:
    print(f"'{test}' is a palindrome: {is_palindrome(test)}")