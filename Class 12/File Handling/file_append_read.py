# Write text to the file
with open("hello.txt", "a") as file:
    file.write(
        "Welcome my class\n"
        "It is a fun place\n"
        "You will learn and play\n"
    )

# Read and display the file contents
with open("hello.txt", "r") as file:
    print(file.read())


# Using same file handle
# with open("hello.txt", "a+") as file:
#    file.write(
#        "Welcome my class\n"
#        "It is a fun place\n"
#        "You will learn and play\n"
#    )
#
#    file.seek(0)  # Move to the beginning of the file
#    print(file.read())    