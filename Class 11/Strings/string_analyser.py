str1 = input("Enter a string: ")

maxlength = 0
maxword = ""

# Split the string into words
words = str1.split()
word_count = len(words)

# Find longest alphabet-only word
for word in words:
    if word.isalpha() and len(word) > maxlength:
        maxlength = len(word)
        maxword = word

# Counters
alphacount = ucount = lcount = dcount = specialcount = 0

# Character analysis
for ch in str1:
    if ch.isalpha():
        alphacount += 1
        if ch.isupper():
            ucount += 1
        else:
            lcount += 1
    elif ch.isdigit():
        dcount += 1
    elif not ch.isspace():   # ignore space
        specialcount += 1

# Output
print("The number of alphabets is:", alphacount)
print("The number of uppercase is:", ucount)
print("The number of lowercase is:", lcount)
print("The number of digits is:", dcount)
print("The number of words is:", word_count)
print("The number of special characters is:", specialcount)
print("Substring with maximum length is:", maxword)
