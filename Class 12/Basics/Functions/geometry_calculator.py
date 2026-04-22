import math

# ---------------------- Helper Functions ---------------------- #
def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be greater than zero. Try again.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def display(value):
    return round(value, 2)

# ---------------------- 2D Shapes ---------------------- #
def circle():
    print("\n--- Circle ---")
    r = get_positive_float("Enter radius: ")
    area = math.pi * r**2
    circumference = 2 * math.pi * r

    print("Area =", display(area), "units²")
    print("Circumference =", display(circumference), "units")

def square():
    print("\n--- Square ---")
    s = get_positive_float("Enter side: ")
    print("Area =", display(s**2), "units²")
    print("Perimeter =", display(4*s), "units")

def rectangle():
    print("\n--- Rectangle ---")
    l = get_positive_float("Enter length: ")
    b = get_positive_float("Enter breadth: ")
    print("Area =", display(l*b), "units²")
    print("Perimeter =", display(2*(l+b)), "units")

def triangle():
    print("\n--- Triangle ---")
    print("1. Base & Height")
    print("2. Heron's Formula (3 sides)")

    choice = input("Choose method: ")

    if choice == "1":
        base = get_positive_float("Enter base: ")
        height = get_positive_float("Enter height: ")
        area = 0.5 * base * height
        print("Area =", display(area), "units²")

    elif choice == "2":
        a = get_positive_float("Side 1: ")
        b = get_positive_float("Side 2: ")
        c = get_positive_float("Side 3: ")

        if a + b > c and a + c > b and b + c > a:
            s = (a + b + c) / 2
            area = math.sqrt(s*(s-a)*(s-b)*(s-c))
            print("Area =", display(area), "units²")
            print("Perimeter =", display(a+b+c), "units")
        else:
            print("Invalid triangle sides!")

    else:
        print("Invalid choice!")

# ---------------------- 3D Shapes ---------------------- #
def cylinder():
    print("\n--- Cylinder ---")
    r = get_positive_float("Enter radius: ")
    h = get_positive_float("Enter height: ")

    csa = 2 * math.pi * r * h
    tsa = 2 * math.pi * r * (h + r)
    volume = math.pi * r**2 * h

    print("Curved Surface Area =", display(csa))
    print("Total Surface Area =", display(tsa))
    print("Volume =", display(volume))

def sphere():
    print("\n--- Sphere ---")
    r = get_positive_float("Enter radius: ")

    tsa = 4 * math.pi * r**2
    volume = (4/3) * math.pi * r**3

    print("Surface Area =", display(tsa))
    print("Volume =", display(volume))

def hemisphere():
    print("\n--- Hemisphere ---")
    r = get_positive_float("Enter radius: ")

    csa = 2 * math.pi * r**2
    tsa = 3 * math.pi * r**2
    volume = (2/3) * math.pi * r**3

    print("Curved Surface Area =", display(csa))
    print("Total Surface Area =", display(tsa))
    print("Volume =", display(volume))

def cone():
    print("\n--- Cone ---")
    r = get_positive_float("Enter radius: ")
    h = get_positive_float("Enter height: ")

    l = math.sqrt(r**2 + h**2)  # slant height

    csa = math.pi * r * l
    tsa = math.pi * r * (l + r)
    volume = (1/3) * math.pi * r**2 * h

    print("Curved Surface Area =", display(csa))
    print("Total Surface Area =", display(tsa))
    print("Volume =", display(volume))

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
while True:
    print("\n====== GEOMETRY CALCULATOR ======")
    for key, (name, _) in menu.items():
        print(f"{key}. {name}")

    choice = input("Enter your choice: ").strip()

    if choice == "0":
        print("Goodbye!")
        break
    elif choice in menu:
        menu[choice][1]()
    else:
        print("Invalid choice! Try again.")