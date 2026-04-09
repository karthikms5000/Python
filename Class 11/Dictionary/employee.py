num = int(input("Enter the number of employees whose data to be stored: "))
employee = {}

for i in range(num):
    name = input("Enter the name of the employee: ")
    salary = float(input("Enter the salary: "))
    employee[name] = salary

print("\nEMPLOYEE NAME\t\tSALARY")
print("-" * 50)

for name, salary in employee.items():
    print(name, "\t\t\t", salary, sep="")
