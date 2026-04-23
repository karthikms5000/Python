import math

# ---------------------- Utility Functions ---------------------- #
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(" Value must be greater than zero. Try again.")
            else:
                return value
        except ValueError:
            print(" Invalid input! Please enter a valid number.")

def get_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(" Invalid choice! Try again.")

def display(value):
    return round(value, 2)

def pause():
    input("\n Press Enter to continue...")

# ---------------------- Calculation Logic ---------------------- #
# 2D Shapes
def calc_circle(r):
    return {
        "Area": math.pi * r**2,
        "Circumference": 2 * math.pi * r
    }

def calc_square(s):
    return {
        "Area": s**2,
        "Perimeter": 4 * s
    }

def calc_rectangle(l, b):
    return {
        "Area": l * b,
        "Perimeter": 2 * (l + b)
    }

def calc_triangle_base_height(base, height):
    return {
        "Area": 0.5 * base * height
    }

def calc_triangle_heron(a, b, c):
    if not (a + b > c and a + c > b and b + c > a):
        return None
    s = (a + b + c) / 2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return {
        "Area": area,
        "Perimeter": a + b + c
    }

# 3D Shapes
def calc_cylinder(r, h):
    return {
        "Curved Surface Area": 2 * math.pi * r * h,
        "Total Surface Area": 2 * math.pi * r * (h + r),
        "Volume": math.pi * r**2 * h
    }

def calc_sphere(r):
    return {
        "Surface Area": 4 * math.pi * r**2,
        "Volume": (4/3) * math.pi * r**3
    }

def calc_hemisphere(r):
    return {
        "Curved Surface Area": 2 * math.pi * r**2,
        "Total Surface Area": 3 * math.pi * r**2,
        "Volume": (2/3) * math.pi * r**3
    }

def calc_cone(r, h):
    l = math.sqrt(r**2 + h**2)
    return {
        "Curved Surface Area": math.pi * r * l,
        "Total Surface Area": math.pi * r * (l + r),
        "Volume": (1/3) * math.pi * r**2 * h
    }

# ---------------------- Display Function ---------------------- #
def print_results(results):
    for key, value in results.items():
        if "Area" in key:
            unit = "units²"
        elif "Volume" in key:
            unit = "units³"
        else:
            unit = "units"
        print(f"{key} = {display(value)} {unit}")

# ---------------------- Shape Handlers ---------------------- #
def circle():
    print("\n--- Circle ---")
    r = get_positive_float("Enter radius: ")
    print_results(calc_circle(r))
    pause()

def square():
    print("\n--- Square ---")
    s = get_positive_float("Enter side: ")
    print_results(calc_square(s))
    pause()

def rectangle():
    print("\n--- Rectangle ---")
    l = get_positive_float("Enter length: ")
    b = get_positive_float("Enter breadth: ")
    print_results(calc_rectangle(l, b))
    pause()

def triangle():
    while True:
        print("\n--- Triangle ---")
        print("1. Base & Height")
        print("2. Heron's Formula")
        print("0. Back")

        choice = get_choice("Choose method: ", {"1", "2", "0"})

        if choice == "1":
            base = get_positive_float("Enter base: ")
            height = get_positive_float("Enter height: ")
            print_results(calc_triangle_base_height(base, height))
            pause()

        elif choice == "2":
            a = get_positive_float("Side 1: ")
            b = get_positive_float("Side 2: ")
            c = get_positive_float("Side 3: ")

            result = calc_triangle_heron(a, b, c)
            if result:
                print_results(result)
            else:
                print(" Invalid triangle sides!")
            pause()

        elif choice == "0":
            break

def cylinder():
    print("\n--- Cylinder ---")
    r = get_positive_float("Enter radius: ")
    h = get_positive_float("Enter height: ")
    print_results(calc_cylinder(r, h))
    pause()

def sphere():
    print("\n--- Sphere ---")
    r = get_positive_float("Enter radius: ")
    print_results(calc_sphere(r))
    pause()

def hemisphere():
    print("\n--- Hemisphere ---")
    r = get_positive_float("Enter radius: ")
    print_results(calc_hemisphere(r))
    pause()

def cone():
    print("\n--- Cone ---")
    r = get_positive_float("Enter radius: ")
    h = get_positive_float("Enter height: ")
    print_results(calc_cone(r, h))
    pause()

# ---------------------- Menu ---------------------- #
menu = {
    "1": ("Circle", circle),
    "2": ("Square", square),
    "3": ("Rectangle", rectangle),
    "4": ("Triangle", triangle),
    "5": ("Cylinder", cylinder),
    "6": ("Sphere", sphere),
    "7": ("Hemisphere", hemisphere),
    "8": ("Cone", cone),
    "0": ("Exit", None)
}

# ---------------------- Main Loop ---------------------- #
def main():
    while True:
        print("\n====== GEOMETRY CALCULATOR ======")
        for key, (name, _) in menu.items():
            print(f"{key}. {name}")

        choice = get_choice("Enter your choice: ", menu.keys())

        if choice == "0":
            print(" Goodbye!")
            break

        menu[choice][1]()

# ---------------------- Entry Point ---------------------- #
if __name__ == "__main__":
    main()
