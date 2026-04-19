import math

# Result type constants (for cleaner logic)
NOT_EQUATION = "not_equation"
LINEAR = "linear"
REAL = "real"
COMPLEX = "complex"
REPEATED = "repeated"

def format_equation(a, b, c):
    sign_b = '+' if b >= 0 else '-'
    sign_c = '+' if c >= 0 else '-'

    return str(a) + "x^2 " + sign_b + " " + str(abs(b)) + "x " + sign_c + " " + str(abs(c)) + " = 0"

def solve_quadratic(a, b, c):
    """
    Solves ax^2 + bx + c = 0
    Returns:
{
    "root1": x1,
    "root2": x2,
    "type": type_string
}
    """

    # Case 1: 'a' is 0 → not a quadratic equation
    if a == 0:
        # If both a and b are 0 → not an equation at all
        if b == 0:
            return {"root1": None, "root2": None, "type": NOT_EQUATION}
        else:
            # Linear equation: bx + c = 0 → x = -c / b
            root = -c / b
            return {"root1": root, "root2": None, "type": LINEAR}

    # Step 1: Calculate the discriminant
    # Discriminant = b^2 - 4ac
    d = b * b - 4 * a * c

    # Case 2: Discriminant is non-negative → real roots
    if d > 0:
        # Square root of discriminant
        sqrt_d = math.sqrt(d)

        # Numerically stable computation:
        # Avoids loss of precision when b is large
        if b >= 0:
            q = -0.5 * (b + sqrt_d)
        else:
            q = -0.5 * (b - sqrt_d)

        # First root
        x1 = q / a

        # Second root (avoid division by zero)
        if q != 0:
            x2 = c / q
        else:
            x2 = x1   # both roots are same

        return {"root1": x1, "root2": x2, "type": REAL}

    # Case 3: Repeated root
    elif d == 0:
        x = -b / (2 * a)
        return {"root1": x, "root2": x, "type": REPEATED}

    # Case 4: Discriminant is negative → complex roots
    else:
        # Compute square root of |discriminant|
        sqrt_d = math.sqrt(-d)

        # Real part is same for both roots
        real_part = -b / (2 * a)

        # Imaginary part
        imag_part = sqrt_d / (2 * a)

        # Construct complex numbers
        x1 = complex(real_part, imag_part)
        x2 = complex(real_part, -imag_part)

        return {"root1": x1, "root2": x2, "type": COMPLEX}


def main():
    print("Quadratic Equation Solver (ax^2 + bx + c = 0)")
    print("Enter 'q' anytime to quit.\n")

    # Infinite loop → keeps solving until user quits
    while True:
        try:
            # Take input for coefficient a
            a_input = input("Enter coefficient a: ").strip()
            if a_input.lower() == 'q':
                break

            # Take input for coefficient b
            b_input = input("Enter coefficient b: ").strip()
            if b_input.lower() == 'q':
                break

            # Take input for coefficient c
            c_input = input("Enter coefficient c: ").strip()
            if c_input.lower() == 'q':
                break

            # Convert inputs to float    
            a = float(a_input)
            b = float(b_input)
            c = float(c_input)

            # Display the equation entered by the user
            print("\nEquation:", format_equation(a, b, c))

            # Solve the equation
            result = solve_quadratic(a, b, c)
            x1 = result["root1"]
            x2 = result["root2"]
            info = result["type"]   # Display type of solution

            # Display results based on type
            if info == NOT_EQUATION:
                print("Type: Not an equation")
                print("No valid solution.\n")

            elif info == LINEAR:
                print("Type: Linear equation")
                print("Root:", x1, "\n")

            elif info == REAL:
                print("Type: Two real roots")
                print("Root 1:", x1)
                print("Root 2:", x2, "\n")

            elif info == REPEATED:
                print("Type: One real root (repeated)")
                print("Root:", x1, "\n")

            elif info == COMPLEX:
                print("Type: Complex roots")
                print("Root 1:", x1)
                print("Root 2:", x2, "\n")

        # Handle invalid numeric input
        except ValueError:
            print("Invalid input. Please enter numeric values.\n")

        # Catch any unexpected errors
        except Exception as e:
            print("An unexpected error occurred:", e, "\n")

    print("Goodbye!")


# Run the program
if __name__ == "__main__":
    main()