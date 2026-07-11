with open("friends.txt", "a") as f:
    while True:
        choice = input("Add another friend? (y/n) : ").strip().lower()
        if choice in ("y", "n"):
            break
        print("Please enter y or n.")
    
    while choice.lower() == "y":
        frnd_name = input("Enter friend's name: ")
        phone = input("Enter friend's mobile number: ")
        e_mail = input("Enter friend's email address: ")
        city = input("Enter friend's current city: ")
        dob = input("Enter friend's date of birth: ")
        age = input("Enter friend's age: ")

        f.write(frnd_name + ", " + phone + ", " + e_mail + ", " + city + ", " + dob + ", " + age + "\n")

        choice = input("Add another friend? (y/n): ")
