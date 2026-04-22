character = input('Enter a character: ').strip()

if len(character) != 1 or not character.isalpha():
    print('Please enter a single alphabet character.')
else:
    if character.lower() in 'aeiou':
        print(character, 'is a vowel')
    else:
        print(character, 'is a consonant')