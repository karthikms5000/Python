students = {}
n = int(input("Enter the number of students: "))

for i in range(n):
    adm_no = int(input("Enter the adm no: "))
    roll_no = int(input("Enter the roll no: "))
    name = input("Enter the student's name: ")
    mark = float(input("Enter the mark: "))
    print()
    
    students[adm_no] = (roll_no, name, mark)

print("\nStudent Details:")
for adm_no, value in students.items():
    print("\nAdmission no: ", adm_no)
    print("Roll no\t\tName\t\tMarks")
    for item in value:
        print(item, end="\t\t")
    print()
