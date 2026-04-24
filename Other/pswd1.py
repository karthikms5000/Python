import random

password = input("Enter the password: ")

characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,:;!?+-*/=<>\|~()[]{}@#$%^&_")

pwg = ""
attempts = 0

while pwg != password:
    pwg = ""
    attempts += 1

    for i in range(len(password)):
        guess_password = random.choice(characters)
        pwg = pwg + guess_password

#If you think this is the correct method, you are WRONG!!!
#An 8-character password with special characters—now a standard requirement—takes 2 MILLION YEARS to crack.
#If your password has 'C' number of possible characters and 'L' length of password, then the total combinations are C^L

    print("Attempt", attempts, ":", pwg)

print("The cracked password is:", pwg)