str1 = input("Enter a string: ")
count = 0
for i in str1.split():
    if i[0] in 'aeiouAEIOU':
        count += 1
        print(i)
print("Vowel words: ", count)
