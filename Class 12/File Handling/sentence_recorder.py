def main():
    try:
        with open("report.txt", "w+", encoding="utf-8") as file:
            while True:
                # Get a non-empty sentence
                while True:
                    sentence = input("Enter a sentence: ").strip()
                    if sentence:
                        file.write(sentence + "\n")
                        break
                    print("Sentence cannot be empty. Please try again.")

                # Validate user's choice
                while True:
                    choice = input("Add more? (y/n): ").strip().lower()

                    if choice in ("y", "n"):
                        break

                    print("Invalid input. Please enter 'y' or 'n'.")

                if choice == "n":
                    break

            # Display current byte position
            print(f"\nCurrent byte position: {file.tell()}")

            # Read file contents
            file.seek(0)
            print("\nContents of the file:")
            print(file.read())

    except FileNotFoundError:
        print("Error: Unable to create or open the file.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except KeyboardInterrupt:
        print("\nOperation cancelled by the user.")

    except OSError as e:
        print(f"File error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()