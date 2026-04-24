import math


def get_angle_unit():
    while True:
        print("\nSelect angle unit:")
        print("1. Degrees")
        print("2. Radians")

        unit = input("Choice: ").strip()
        if unit in {"1", "2"}:
            return unit

        print("Invalid choice.\n")


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def calculate_log10(x):
    if x <= 0:
        raise ValueError("log10 undefined for non-positive numbers")
    return math.log10(x)


# Mapping for trig functions (except tan, handled separately)
TRIG_FUNCTIONS = {
    2: ("sin", math.sin),
    3: ("cos", math.cos),
}


while True:
    print("\n--- Calculator Menu ---")
    print("1. log10(x)")
    print("2. sin(x)")
    print("3. cos(x)")
    print("4. tan(x)")
    print("5. Exit")

    choice = input("Enter your choice (1-5 or q to quit): ").strip().lower()

    if choice == "q":
        print("Exiting program...")
        break

    if not choice.isdigit():
        print("Invalid input. Please enter a number between 1 and 5.")
        continue

    choice = int(choice)

    if choice not in {1, 2, 3, 4, 5}:
        print("Invalid choice. Please select a number from 1 to 5.")
        continue

    if choice == 5:
        print("Exiting program...")
        break

    # --- LOG10 ---
    if choice == 1:
        x = get_number("Enter a positive number: ")
        try:
            result = calculate_log10(x)
            print(f"log10({x}) = {result:.6f}")
        except ValueError:
            print("Error: log10 is defined only for positive numbers.")

    # --- TRIG FUNCTIONS ---
    elif choice in {2, 3, 4}:
        unit = get_angle_unit()
        angle = get_number("Enter angle: ")

        # Convert to radians if needed
        rad = math.radians(angle) if unit == "1" else angle

        # Warn for very large values (precision issue)
        if abs(rad) > 1e10:
            print("Warning: Very large angle may reduce accuracy.")

        # --- TAN ---
        if choice == 4:
            cos_val = math.cos(rad)
            if abs(cos_val) < 1e-12:
                print("tan is undefined or numerically unstable for this angle.")
            else:
                print(f"tan({rad}) = {math.tan(rad):.6f}")

        # --- SIN / COS ---
        else:
            name, func = TRIG_FUNCTIONS[choice]
            print(f"{name}({rad}) = {func(rad):.6f}")