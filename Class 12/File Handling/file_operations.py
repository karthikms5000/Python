# Global variable to hold the currently open file (for seek and tell operations)
current_file = None
CHARSET = 'utf-8'  # Default encoding for file operations

def is_file_open(file_obj):
    """Check if a file object is still open."""
    if file_obj is None:
        return False
    return not file_obj.closed

def create_new_file():
    """Create a new file. Ask for filename and create it (empty or with initial content)."""
    filename = input("Enter the filename to create: ")
    if not filename.strip():
        print("Error: Filename cannot be empty.")
        return
    try:
        with open(filename, 'w', encoding=CHARSET) as file:
            content = input("Enter initial content (leave empty for blank file): ")
            file.write(content)
        print(f"File '{filename}' created successfully.")
    except PermissionError:
        print("Error: Permission denied. Cannot create the file.")
    except OSError as e:
        print(f"Error: Cannot create file - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def open_existing_file():
    """Open an existing file and keep it open for seek/tell operations."""
    global current_file
    if is_file_open(current_file):
        current_file.close()
    filename = input("Enter the filename to open: ")
    try:
        current_file = open(filename, 'r+', encoding=CHARSET)  # Open in read-write mode to allow seek/tell
        print(f"File '{filename}' opened successfully.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except OSError as e:
        print(f"Error: Cannot open file - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_to_file():
    """Write to a file (overwrite). Ask for filename and content."""
    filename = input("Enter the filename to write to: ")
    if not filename.strip():
        print("Error: Filename cannot be empty.")
        return
    try:
        with open(filename, 'w', encoding=CHARSET) as file:
            content = input("Enter content to write: ")
            file.write(content)
        print("Content written successfully.")
    except PermissionError:
        print("Error: Permission denied.")
    except OSError as e:
        print(f"Error: Cannot write to file - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def write_multiple_lines():
    """Write multiple lines to a file using writelines(). Ask for filename and lines."""
    filename = input("Enter the filename to write to: ")
    if not filename.strip():
        print("Error: Filename cannot be empty.")
        return
    try:
        lines = []
        print("Enter lines (press Enter on empty line to stop):")
        while True:
            line = input()
            if not line:
                break
            lines.append(line + '\n')  # Add newline for each line
        if not lines:
            print("Warning: No lines entered. File will be created empty.")
        with open(filename, 'w', encoding=CHARSET) as file:
            file.writelines(lines)
        print("Lines written successfully.")
    except PermissionError:
        print("Error: Permission denied.")
    except OSError as e:
        print(f"Error: Cannot write to file - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_entire_file():
    """Read entire file using read(). Ask for filename."""
    filename = input("Enter the filename to read: ")
    if not filename.strip():
        print("Error: Filename cannot be empty.")
        return
    try:
        with open(filename, 'r', encoding=CHARSET) as file:
            content = file.read()
            if not content:
                print("File is empty.")
            else:
                print("File content:")
                print(content)
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except UnicodeDecodeError:
        print(f"Error: Cannot decode file with {CHARSET} encoding.")
    except OSError as e:
        print(f"Error: Cannot read file - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_one_line():
    """Read one line using readline(). Ask for filename."""
    filename = input("Enter the filename to read: ")
    if not filename.strip():
        print("Error: Filename cannot be empty.")
        return
    try:
        with open(filename, 'r', encoding=CHARSET) as file:
            line = file.readline()
            if not line:
                print("File is empty.")
            else:
                print("First line:")
                print(line.strip())  # Strip to remove trailing newline
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except UnicodeDecodeError:
        print(f"Error: Cannot decode file with {CHARSET} encoding.")
    except OSError as e:
        print(f"Error: Cannot read file - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def show_pointer_position():
    """Show current file pointer position using tell()."""
    if is_file_open(current_file):
        try:
            position = current_file.tell()
            print(f"Current file pointer position: {position}")
        except OSError as e:
            print(f"Error: Cannot determine file position - {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Error: No file is currently open.")

def move_pointer():
    """Move file pointer using seek(). Ask for position and whence."""
    if is_file_open(current_file):
        try:
            position = int(input("Enter position to seek: "))
            if position < 0:
                print("Error: Position cannot be negative.")
                return
            whence = input("Enter whence (0 for start, 1 for current, 2 for end, default 0): ")
            whence = int(whence) if whence else 0
            if whence not in [0, 1, 2]:
                print("Error: Invalid whence value. Must be 0, 1, or 2.")
                return
            current_file.seek(position, whence)
            new_position = current_file.tell()
            print(f"Pointer moved successfully. New position: {new_position}")
        except ValueError:
            print("Error: Invalid position or whence. Must be integers.")
        except OSError as e:
            print(f"Error: Cannot seek file - {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
    else:
        print("Error: No file is currently open.")

def traverse_file():
    """Traverse file content line by line. Ask for filename."""
    filename = input("Enter the filename to traverse: ")
    if not filename.strip():
        print("Error: Filename cannot be empty.")
        return
    try:
        with open(filename, 'r', encoding=CHARSET) as file:
            line_count = 0
            for line_num, line in enumerate(file, 1):
                print(f"Line {line_num}: {line.strip()}")
                line_count += 1
            if line_count == 0:
                print("File is empty.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied.")
    except UnicodeDecodeError:
        print(f"Error: Cannot decode file with {CHARSET} encoding.")
    except OSError as e:
        print(f"Error: Cannot read file - {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to display menu and handle user choices."""
    while True:
        print("\nMenu:")
        print("1. Create a new file")
        print("2. Open an existing file")
        print("3. Write to file (overwrite)")
        print("4. Write multiple lines using writelines()")
        print("5. Read entire file using read()")
        print("6. Read one line using readline()")
        print("7. Show current file pointer position using tell()")
        print("8. Move file pointer using seek()")
        print("9. Traverse file content line by line")
        print("10. Exit")
        
        choice = input("Enter your choice (1-10): ")
        try:
            choice = int(choice)
            if choice == 1:
                create_new_file()
            elif choice == 2:
                open_existing_file()
            elif choice == 3:
                write_to_file()
            elif choice == 4:
                write_multiple_lines()
            elif choice == 5:
                read_entire_file()
            elif choice == 6:
                read_one_line()
            elif choice == 7:
                show_pointer_position()
            elif choice == 8:
                move_pointer()
            elif choice == 9:
                traverse_file()
            elif choice == 10:
                if is_file_open(current_file):
                    current_file.close()
                    print("File closed.")
                print("Exiting program.")
                break
            else:
                print("Error: Invalid choice. Please enter a number between 1 and 10.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

# Run the main function
if __name__ == "__main__":
    main()