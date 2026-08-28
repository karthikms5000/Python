def capitalize_sentence():
    try:
        with (
            open("test_report.txt", "r") as source,
            open("file1.txt", "w") as destination
        ):
            capitalize_next = True

            for line in source:
                result = []

                for ch in line:
                    if capitalize_next and ch.isalpha():
                        result.append(ch.upper())
                        capitalize_next = False
                    else:
                        result.append(ch)

                    if ch in ".!?":      # Capitalize after ., !, or ?
                        capitalize_next = True

                destination.write("".join(result))

        print("File processed successfully.")

    except FileNotFoundError:
        print("Source file does not exist.")
    except IOError:
        print("An error occurred while reading or writing the file.")


capitalize_sentence()
