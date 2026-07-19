import os
import pickle

# Accepting data for Dictionary
def insertRec():
    rollno = int(input("Enter roll number: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    # Creating the Dictionary
    rec = {"Rollno": rollno, "Name": name, "Marks": marks}

    # Writing the Dictionary
    with open("student.dat", "ab") as f:
        pickle.dump(rec, f)

    print("Record inserted successfully.\n")


# Reading all records
def readRec():
    if not os.path.exists("student.dat"):
        print("No records found.\n")
        return

    with open("student.dat", "rb") as f:
        print("\n----- Student Records -----")
        while True:
            try:
                rec = pickle.load(f)
                print("Roll No :", rec["Rollno"])
                print("Name    :", rec["Name"])
                print("Marks   :", rec["Marks"])
                print("--------------------------")
            except EOFError:
                break


# Searching a record based on Roll Number
def searchRollNo(r):
    if not os.path.exists("student.dat"):
        print("No records found.\n")
        return

    flag = False

    with open("student.dat", "rb") as f:
        while True:
            try:
                rec = pickle.load(f)
                if rec["Rollno"] == r:
                    print("\nRecord Found")
                    print("Roll No :", rec["Rollno"])
                    print("Name    :", rec["Name"])
                    print("Marks   :", rec["Marks"])
                    flag = True
                    break
            except EOFError:
                break

    if not flag:
        print("Record not found.\n")


# Updating marks for a Roll Number
def updateMarks(r, m):
    if not os.path.exists("student.dat"):
        print("No records found.\n")
        return

    reclst = []

    with open("student.dat", "rb") as f:
        while True:
            try:
                rec = pickle.load(f)
                reclst.append(rec)
            except EOFError:
                break

    flag = False

    for rec in reclst:
        if rec["Rollno"] == r:
            rec["Marks"] = m
            flag = True
            break

    if flag:
        with open("student.dat", "wb") as f:
            for rec in reclst:
                pickle.dump(rec, f)
        print("Record updated successfully.\n")
    else:
        print("Record not found.\n")


# Deleting a record based on Roll Number
def deleteRec(r):
    if not os.path.exists("student.dat"):
        print("No records found.\n")
        return

    reclst = []

    with open("student.dat", "rb") as f:
        while True:
            try:
                rec = pickle.load(f)
                reclst.append(rec)
            except EOFError:
                break

    flag = False

    with open("student.dat", "wb") as f:
        for rec in reclst:
            if rec["Rollno"] == r:
                flag = True
                continue
            pickle.dump(rec, f)

    if flag:
        print("Record deleted successfully.\n")
    else:
        print("Record not found.\n")


# Main Menu
while True:
    print("\n========== STUDENT RECORD MENU ==========")
    print("1. Insert Record")
    print("2. Display All Records")
    print("3. Search Record")
    print("4. Update Marks")
    print("5. Delete Record")
    print("0. Exit")
    print("=========================================")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Thank you! Exiting program...")
        break

    elif choice == 1:
        insertRec()

    elif choice == 2:
        readRec()

    elif choice == 3:
        r = int(input("Enter Roll Number to search: "))
        searchRollNo(r)

    elif choice == 4:
        r = int(input("Enter Roll Number: "))
        m = int(input("Enter New Marks: "))
        updateMarks(r, m)

    elif choice == 5:
        r = int(input("Enter Roll Number: "))
        deleteRec(r)

    else:
        print("Invalid Choice! Please try again.\n")