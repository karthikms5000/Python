def print_lines_starting_with_you():
    with open("alpha.txt", "r") as f:
        for line in f:
            if line.lstrip().startswith("You"):
                print(line, end="")

print_lines_starting_with_you()