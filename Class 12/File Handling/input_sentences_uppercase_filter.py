# Program to accept sentences until the user enters "END",
# save them to a text file, and display only those sentences
# that begin with an uppercase alphabet.

filename = "sentences.txt"

# Accept input and save to file
with open(filename, "w") as file:
    print("Enter sentences (type 'END' to stop):")

    while True:
        sentence = input()

        if sentence == "END":
            break

        file.write(sentence + "\n")

# Read the file and display sentences
print("\nSentences beginning with an uppercase alphabet:")

with open(filename, "r") as file:
    for line in file:
        sentence = line.strip()

        if sentence and sentence[0].isupper():
            print(sentence)