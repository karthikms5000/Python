import os
import pickle

DATA_FILE = "student.dat"


def read_records():
    """Generator that yields all student records from the data file."""
    if not os.path.exists(DATA_FILE):
        return

    with open(DATA_FILE, "rb") as file:
        while True:
            try:
                yield pickle.load(file)
            except EOFError:
                break


def load_all_records():
    """Return all student records as a list."""
    return list(read_records())


def get_integer(prompt, minimum = None, maximum = None):
    """Read an integer from the user with optional range validation."""
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Value must be at least {minimum}.")
                continue

            if maximum is not None and value > maximum:
                print(f"Value must not exceed {maximum}.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def save_all_records(student_records):
    """Write all records back to the data file."""
    with open(DATA_FILE, "wb") as file:
        for student_record in student_records:
            pickle.dump(student_record, file)


def insert_record():
    """Insert a new student record into the data file."""

    roll_number = get_integer("Enter roll number: ", minimum = 1)

    # Prevent duplicate roll numbers
    for student_record in read_records():
        if student_record["Rollno"] == roll_number:
            print("A record with this roll number already exists.\n")
            return

    student_name = input("Enter Name: ")
    marks = get_integer("Enter Marks: ", minimum = 0, maximum = 100)

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

    print("\n----- Student Records -----")

    for student_record in read_records():
        print("Roll No :", student_record["Rollno"])
        print("Name    :", student_record["Name"])
        print("Marks   :", student_record["Marks"])
        print("--------------------------")


def search_record_by_roll_number(roll_number):
    """Search for a student record by roll number."""

    if not os.path.exists(DATA_FILE):
        print("No records found.\n")
        return

    for student_record in read_records():
        if student_record["Rollno"] == roll_number:
            print("\nRecord Found")
            print("Roll No :", student_record["Rollno"])
            print("Name    :", student_record["Name"])
            print("Marks   :", student_record["Marks"])
            return

    print("Record not found.\n")


def update_student_marks(roll_number, new_marks):
    """Update marks for the specified roll number."""

    if not os.path.exists(DATA_FILE):
        print("No records found.\n")
        return

    student_records = load_all_records()

    for student_record in student_records:
        if student_record["Rollno"] == roll_number:
            student_record["Marks"] = new_marks
            save_all_records(student_records)
            print("Record updated successfully.\n")
            return

    print("Record not found.\n")


def delete_record(roll_number):
    """Delete a student record by roll number."""

    if not os.path.exists(DATA_FILE):
        print("No records found.\n")
        return

    student_records = load_all_records()

    filtered_records = [
        record for record in student_records
        if record["Rollno"] != roll_number
    ]

    if len(filtered_records) == len(student_records):
        print("Record not found.\n")
        return

    confirm = input(f"Are you sure you want to delete Roll Number {roll_number}? (y/n): ").strip().lower()

    if confirm != "y":
        print("Deletion cancelled.\n")
        return

    save_all_records(filtered_records)
    print("Record deleted successfully.\n")


def display_menu():
    """Display the main menu."""
    print("\n========== STUDENT RECORD MENU ==========")
    print("1. Insert Record")
    print("2. Display All Records")
    print("3. Search Record")
    print("4. Update Marks")
    print("5. Delete Record")
    print("0. Exit")
    print("=========================================")


def run():
    """Run the user interface."""

    while True:
        display_menu()

        menu_choice = get_integer("Enter your choice: ", minimum = 0, maximum = 5)

        if menu_choice == 0:
            print("Thank you! Exiting program...")
            break

        elif menu_choice == 1:
            insert_record()

        elif menu_choice == 2:
            display_all_records()

        elif menu_choice == 3:
            roll_number = get_integer("Enter Roll Number to search: ", minimum = 1)
            search_record_by_roll_number(roll_number)

        elif menu_choice == 4:
            roll_number = get_integer("Enter Roll Number: ", minimum = 1)
            new_marks = get_integer("Enter New Marks: ", minimum = 0, maximum = 100)
            update_student_marks(roll_number, new_marks)

        elif menu_choice == 5:
            roll_number = get_integer("Enter Roll Number: ", minimum = 1)
            delete_record(roll_number)

        else:
            print("Invalid Choice! Please try again.\n")


if __name__ == "__main__":
    run()