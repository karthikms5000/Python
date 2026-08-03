import os
import pickle

DATA_FILE = "student.dat"


def insert_record():
    """Insert a new student record into the data file."""
    roll_number = int(input("Enter roll number: "))
    student_name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    student_record = {
        "Rollno": roll_number,
        "Name": student_name,
        "Marks": marks,
    }

    with open(DATA_FILE, "ab") as file:
        pickle.dump(student_record, file)

    print("Record inserted successfully.\n")


def display_all_records():
    """Display all student records."""
    if not os.path.exists(DATA_FILE):
        print("No records found.\n")
        return

    with open(DATA_FILE, "rb") as file:
        print("\n----- Student Records -----")

        while True:
            try:
                student_record = pickle.load(file)
                print("Roll No :", student_record["Rollno"])
                print("Name    :", student_record["Name"])
                print("Marks   :", student_record["Marks"])
                print("--------------------------")
            except EOFError:
                break


def search_record_by_roll_number(roll_number):
    """Search for a student record by roll number."""
    if not os.path.exists(DATA_FILE):
        print("No records found.\n")
        return

    record_found = False

    with open(DATA_FILE, "rb") as file:
        while True:
            try:
                student_record = pickle.load(file)

                if student_record["Rollno"] == roll_number:
                    print("\nRecord Found")
                    print("Roll No :", student_record["Rollno"])
                    print("Name    :", student_record["Name"])
                    print("Marks   :", student_record["Marks"])
                    record_found = True
                    break

            except EOFError:
                break

    if not record_found:
        print("Record not found.\n")


def update_student_marks(roll_number, new_marks):
    """Update marks for the specified roll number."""
    if not os.path.exists(DATA_FILE):
        print("No records found.\n")
        return

    student_records = []

    with open(DATA_FILE, "rb") as file:
        while True:
            try:
                student_records.append(pickle.load(file))
            except EOFError:
                break

    record_found = False

    for student_record in student_records:
        if student_record["Rollno"] == roll_number:
            student_record["Marks"] = new_marks
            record_found = True
            break

    if record_found:
        with open(DATA_FILE, "wb") as file:
            for student_record in student_records:
                pickle.dump(student_record, file)

        print("Record updated successfully.\n")
    else:
        print("Record not found.\n")


def delete_record(roll_number):
    """Delete a student record by roll number."""
    if not os.path.exists(DATA_FILE):
        print("No records found.\n")
        return

    student_records = []

    with open(DATA_FILE, "rb") as file:
        while True:
            try:
                student_records.append(pickle.load(file))
            except EOFError:
                break

    record_found = False

    with open(DATA_FILE, "wb") as file:
        for student_record in student_records:
            if student_record["Rollno"] == roll_number:
                record_found = True
                continue

            pickle.dump(student_record, file)

    if record_found:
        print("Record deleted successfully.\n")
    else:
        print("Record not found.\n")


while True:
    print("\n========== STUDENT RECORD MENU ==========")
    print("1. Insert Record")
    print("2. Display All Records")
    print("3. Search Record")
    print("4. Update Marks")
    print("5. Delete Record")
    print("0. Exit")
    print("=========================================")

    menu_choice = int(input("Enter your choice: "))

    if menu_choice == 0:
        print("Thank you! Exiting program...")
        break

    if menu_choice == 1:
        insert_record()

    elif menu_choice == 2:
        display_all_records()

    elif menu_choice == 3:
        roll_number = int(input("Enter Roll Number to search: "))
        search_record_by_roll_number(roll_number)

    elif menu_choice == 4:
        roll_number = int(input("Enter Roll Number: "))
        new_marks = int(input("Enter New Marks: "))
        update_student_marks(roll_number, new_marks)

    elif menu_choice == 5:
        roll_number = int(input("Enter Roll Number: "))
        delete_record(roll_number)

    else:
        print("Invalid Choice! Please try again.\n")