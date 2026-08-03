import pickle
from pathlib import Path

FILE_NAME = "empfile.dat"


def get_positive_integer(prompt: str) -> int:
    """
    Prompt the user until a valid non-negative integer is entered.
    """
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("Value cannot be negative. Please try again.")
                continue

            return value

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_non_empty_string(prompt: str) -> str:
    """
    Prompt the user until a non-empty string is entered.
    """
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def add_employee_records() -> None:
    """
    Collect employee records from the user and store them
    in a binary file using pickle.
    """

    print("=" * 45)
    print("EMPLOYEE RECORD ENTRY")
    print("=" * 45)

    record_number = 1

    try:
        with open(FILE_NAME, "ab") as binary_file:

            while True:
                print(f"\nRecord #{record_number}")

                employee_number = get_positive_integer(
                    "Employee Number : "
                )

                employee_name = get_non_empty_string(
                    "Employee Name   : "
                )

                basic_salary = get_positive_integer(
                    "Basic Salary    : "
                )

                allowances = get_positive_integer(
                    "Allowances      : "
                )

                total_salary = basic_salary + allowances

                print(f"Total Salary     : {total_salary}")

                employee_record = {
                    "employee_number": employee_number,
                    "employee_name": employee_name,
                    "basic_salary": basic_salary,
                    "allowances": allowances,
                    "total_salary": total_salary,
                }

                pickle.dump(employee_record, binary_file)

                while True:
                    choice = input(
                        "\nAdd another employee? (Y/N): "
                    ).strip().lower()

                    if choice in ("y", "n"):
                        break

                    print("Please enter Y or N.")

                if choice == "n":
                    print("\nRecord entry completed.")
                    print(
                        f"File size: {binary_file.tell()} bytes"
                    )
                    break

                record_number += 1

    except OSError as error:
        print(f"File error: {error}")


def display_employee_records() -> None:
    """
    Read and display all employee records from the binary file.
    """

    print("\n" + "=" * 45)
    print("EMPLOYEE RECORDS")
    print("=" * 45)

    if not Path(FILE_NAME).exists():
        print("No employee file found.")
        return

    try:
        with open(FILE_NAME, "rb") as binary_file:

            record_number = 1

            while True:
                try:
                    employee = pickle.load(binary_file)

                    print(f"\nRecord #{record_number}")
                    print("-" * 30)
                    print(
                        f"Employee Number : {employee['employee_number']}"
                    )
                    print(
                        f"Employee Name   : {employee['employee_name']}"
                    )
                    print(
                        f"Basic Salary    : {employee['basic_salary']}"
                    )
                    print(
                        f"Allowances      : {employee['allowances']}"
                    )
                    print(
                        f"Total Salary    : {employee['total_salary']}"
                    )

                    record_number += 1

                except EOFError:
                    break

    except FileNotFoundError:
        print("Employee file not found.")

    except pickle.UnpicklingError:
        print("The binary file is corrupted or invalid.")

    except OSError as error:
        print(f"File error: {error}")


def main() -> None:
    add_employee_records()
    display_employee_records()


if __name__ == "__main__":
    main()