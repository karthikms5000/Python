text = input("Enter a string: ")
result = ""
for char in text:
    if char not in "aeiouAEIOU":
        result += char
print("String without vowels:", result)
