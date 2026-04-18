import math

def solve_quadratic(a, b, c):
    """
    Solves ax^2 + bx + c = 0
    Returns:
        (root1, root2, description_string)
    """

    # Case 1: 'a' is 0 → not a quadratic equation
    if a == 0:
        # If both a and b are 0 → not an equation at all
        if b == 0:
            return None, None, "Not an equation (a = 0 and b = 0)"
        else:
            # Linear equation: bx + c = 0 → x = -c / b
            root = -c / b
            return root, None, "Linear equation (only one root)"

    # Step 1: Calculate the discriminant
    # Discriminant = b^2 - 4ac
    d = b * b - 4 * a * c

    # Case 2: Discriminant is non-negative → real roots
    if d >= 0:
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
            x2 = x1  # both roots are same

        return x1, x2, "Real roots"

    # Case 3: Discriminant is negative → complex roots
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

        return x1, x2, "Complex roots"


def main():
    print("Quadratic Equation Solver (ax^2 + bx + c = 0)")
    print("Enter 'q' anytime to quit.\n")

    # Infinite loop → keeps solving until user quits
    while True:
        try:
            # Take input for coefficient a
            a_input = input("Enter coefficient a: ")
            if a_input.lower() == 'q':
                break

            # Take input for coefficient b
            b_input = input("Enter coefficient b: ")
            if b_input.lower() == 'q':
                break

            # Take input for coefficient c
            c_input = input("Enter coefficient c: ")
            if c_input.lower() == 'q':
                break

            # Convert inputs to float
            a = float(a_input)
            b = float(b_input)
            c = float(c_input)

            # Display the equation entered by the user
            print("\nEquation: (" + str(a) + ")x^2 + (" + str(b) + ")x + (" + str(c) + ") = 0")

            # Solve the equation
            x1, x2, info = solve_quadratic(a, b, c)

            # Display type of solution
            print("Type:", info)

            # Display results based on type
            if info.startswith("Not"):
                print("No valid solution.\n")

            elif info.startswith("Linear"):
                print("Root:", x1, "\n")

            else:
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