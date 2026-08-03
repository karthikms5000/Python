# Program to store and display item records using a binary file

import pickle

filename = "items.dat"

# Accept number of records
n = int(input("Enter the number of records: "))

# Writing records to binary file
with open(filename, "wb") as f:
    for i in range(n):
        print(f"\nEnter details of Item {i + 1}")
        item_no = int(input("Enter Item Number: "))
        item_name = input("Enter Item Name: ")
        quantity = int(input("Enter Quantity: "))
        price = float(input("Enter Price per Item: "))

        record = [item_no, item_name, quantity, price]
        pickle.dump(record, f)

# Reading and displaying records
print("\nRecords in the file:\n")

with open(filename, "rb") as f:
    while True:
        try:
            record = pickle.load(f)
            amount = record[2] * record[3]

            print("Item No       :", record[0])
            print("Item Name     :", record[1])
            print("Quantity      :", record[2])
            print("Price per item:", record[3])
            print("Amount        :", amount)
            print("-" * 30)

        except EOFError:
            break