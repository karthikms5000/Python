import os


def file_copy(source_path, destination_path):
    """
    Copy the contents of one text file to another.
    """

    # Prevent copying a file onto itself
    if os.path.abspath(source_path) == os.path.abspath(destination_path):
        raise ValueError("Source and destination cannot be the same file.")

    with open(source_path, "r", encoding="utf-8") as source, \
         open(destination_path, "w", encoding="utf-8") as destination:

        # Copy in chunks to handle large files efficiently
        while chunk := source.read(4096):
            destination.write(chunk)


source = input("Enter the source file name: ").strip()
destination = input("Enter the destination file name: ").strip()

try:
    file_copy(source, destination)
    print("File copied successfully!")

except FileNotFoundError:
    print("Error: Source file not found.")

except PermissionError:
    print("Error: Permission denied.")

except ValueError as e:
    print(f"Error: {e}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")