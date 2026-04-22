original = input("Enter the string: ")
str1 = original.lower().replace(" ", "")
left, right = 0, len(str1) - 1

while left < right:
    if str1[left] != str1[right]:
        print(original, "is not a palindrome.")
        break
    left += 1
    right -= 1
else:
    print(original, "is a palindrome.")