from random import randint

password = input("Enter the password: ")

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
              'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
              '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
              '.', ',', ':', ';', '!', '?', '+', '-', '*', '/', '=', '<', '>', '|', '~', '(', ')', '[', ']', '{', '}', '@', '#', '$', '%', '^', '&', '_'
              ]

pwg = ""
attempts = 0

while pwg != password:
    pwg = ""
    attempts += 1

    for i in range(len(password)):
        guess_password = characters[randint(0, 256)]
        pwg = str(guess_password) + str(pwg)
        print(pwg)

print("The cracked password is: ", pwg)        