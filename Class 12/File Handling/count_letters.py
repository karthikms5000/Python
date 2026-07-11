def count_letters():
    with open("words.txt", "r") as f:
        lower = upper = 0
        for character in f.read():
            if character.isupper():
                upper += 1
            elif character.islower():
                lower += 1
        print("Number of uppercase letters : ", upper)
        print("Number of lowercase letters : ", lower)

count_letters()