classxi = {}

no_of_sections = int(input("Enter the number of sections: "))
i = 0

while i < no_of_sections:
    section = input("Enter the section: ")
    section_name = input("Enter the section name: ")
    classxi[section] = section_name
    i += 1

print("Class\tSection\tSection name")
for section in classxi:
    print("XI\t", section, "\t", classxi[section])
