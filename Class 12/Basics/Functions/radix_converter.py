def parse_number(num_str):
    num_str = num_str.strip()
    sign = 1

    if num_str.startswith(("+", "-")):
        if num_str[0] == "-":
            sign = -1
        num_str = num_str[1:]

    num_lower = num_str.lower()

    if num_lower.startswith("0b"):
        base = 2
        num_str = num_str[2:]
    elif num_lower.startswith("0o"):
        base = 8
        num_str = num_str[2:]
    elif num_lower.startswith("0x"):
        base = 16
        num_str = num_str[2:]
    else:
        base = None

    return sign, num_str, base


def char_to_value(c):
    if c.isdigit():
        return int(c)
    return ord(c.upper()) - ord('A') + 10


def is_valid_number(num_str, base):
    try:
        if "." in num_str:
            int_part, frac_part = num_str.split(".", 1)
            if int_part:
                int(int_part, base)
            if frac_part:
                int(frac_part, base)
        else:
            int(num_str, base)
        return True
    except ValueError:
        return False


def convert_to_decimal(num_str, base):
    if "." in num_str:
        int_part, frac_part = num_str.split(".", 1)
    else:
        int_part, frac_part = num_str, ""

    # Integer part
    int_value = int(int_part, base) if int_part else 0

    # Fractional part
    frac_value = 0
    for i, digit in enumerate(frac_part, start=1):
        value = char_to_value(digit)

        if value >= base:
            raise ValueError(f"Invalid digit '{digit}' for base {base}")

        frac_value += value / (base ** i)

    return int_value + frac_value


def from_decimal_fraction(value, base, precision=10):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    for _ in range(precision):
        value *= base
        digit = int(value)
        result.append(digits[digit])
        value -= digit
        if value == 0:
            break

    return "".join(result)


def convert_from_decimal(value, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    sign = "-" if value < 0 else ""
    value = abs(value)

    int_part = int(value)
    frac_part = value - int_part

    # Integer conversion
    if int_part == 0:
        int_str = "0"
    else:
        int_str = ""
        while int_part > 0:
            int_str = digits[int_part % base] + int_str
            int_part //= base

    # Fraction conversion
    if frac_part > 0:
        frac_str = from_decimal_fraction(frac_part, base)
        return f"{sign}{int_str}.{frac_str}"

    return f"{sign}{int_str}"


def format_output(value, base, prefix=""):
    converted = convert_from_decimal(value, base)
    if converted.startswith("-"):
        return "-" + prefix + converted[1:]
    return prefix + converted


def get_base_choice():
    bases = {
        "1": ("Decimal", 10),
        "2": ("Binary", 2),
        "3": ("Octal", 8),
        "4": ("Hexadecimal", 16),
    }

    while True:
        print("\nSelect source base:")
        for k, v in bases.items():
            print(f"{k}. {v[0]}")

        choice = input("Enter choice: ").strip()
        if choice in bases:
            return bases[choice]

        print("Invalid choice.\n")


def get_target_choice():
    while True:
        print("\nTarget:")
        print("1. Decimal")
        print("2. Binary")
        print("3. Octal")
        print("4. Hexadecimal")
        print("5. ALL")

        choice = input("Choice: ").strip()
        if choice in {"1", "2", "3", "4", "5"}:
            return choice

        print("Invalid choice.\n")


def show_history(history):
    if not history:
        print("No history yet.\n")
        return

    print("\n=== Conversion History ===")
    for item in history:
        print(f"{item['input']} (base {item['base']})")
        for line in item["result"]:
            print("  ", line)
        print()


def converter_menu():
    history = []

    while True:
        print("\n=== Number System Converter ===")
        print("1. Convert Number")
        print("2. Show History")
        print("3. Exit")

        choice = input("Select option: ").strip()

        if choice == "1":
            num = input("Enter number: ").strip()

            if not num:
                print("Input cannot be empty.\n")
                continue

            sign, num_clean, detected_base = parse_number(num)

            if detected_base:
                source_base = detected_base
                print(f"Detected base: {source_base}")
            else:
                _, source_base = get_base_choice()

            if not is_valid_number(num_clean, source_base):
                print(f"'{num}' is not valid in base {source_base}\n")
                continue

            decimal_value = sign * convert_to_decimal(num_clean, source_base)

            target = get_target_choice()

            result_lines = []
            print("\n=== Result ===")

            if target == "1":
                line = f"Decimal: {decimal_value}"
                print(line)
                result_lines.append(line)

            elif target == "2":
                val = format_output(decimal_value, 2, "0b")
                line = f"Binary: {val}"
                print(line)
                result_lines.append(line)

            elif target == "3":
                val = format_output(decimal_value, 8, "0o")
                line = f"Octal: {val}"
                print(line)
                result_lines.append(line)

            elif target == "4":
                val = format_output(decimal_value, 16, "0x")
                line = f"Hex: {val}"
                print(line)
                result_lines.append(line)

            elif target == "5":
                outputs = [
                    f"Decimal : {decimal_value}",
                    f"Binary  : {format_output(decimal_value, 2, '0b')}",
                    f"Octal   : {format_output(decimal_value, 8, '0o')}",
                    f"Hex     : {format_output(decimal_value, 16, '0x')}",
                ]

                for line in outputs:
                    print(line)
                    result_lines.append(line)

            history.append({
                "input": num,
                "base": source_base,
                "result": result_lines
            })

        elif choice == "2":
            show_history(history)

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    try:
        converter_menu()
    except KeyboardInterrupt:
        print("\nProgram terminated.")