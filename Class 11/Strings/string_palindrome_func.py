def is_palindrome(text):
    text = text.lower().replace(" ", "")
    left, right = 0, len(text) - 1

    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    return True

user_input = input("Enter the string: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")