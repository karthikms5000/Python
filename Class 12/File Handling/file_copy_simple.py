def file_copy(source_file, destination_file):
    """Copies content from source to destination. Throws exceptions to caller."""
    with (
        open(source_file, "r") as source,
        open(destination_file, "w") as destination
    ):
        destination.write(source.read())

# --- User Interface Layer ---
source = input("Enter the source file name: ")
destination = input("Enter the destination file name: ")

try:
    file_copy(source, destination)
    print("File copied successfully!")
except FileNotFoundError:
    print("Error: Source file not found.")
except PermissionError:
    print("Error: Permission denied.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")