def vowel_count():
    with open("poem.txt", "r") as f:
        count = 0
        for character in f.read().lower():
            if character in "aeiou":
                count += 1
    print("Number of vowels : ", count)
vowel_count()    