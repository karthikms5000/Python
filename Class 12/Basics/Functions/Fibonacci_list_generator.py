def fibonacci_series(n):
    """Return a list containing the first n Fibonacci numbers starting from 0."""
    series = []
    a, b = 0, 1
    
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    
    return series


def main():
    while True:
        try:
            n = int(input("Enter number of terms: "))
            if n > 0:
                break
            print("Please enter a positive integer.")

        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    print("Fibonacci series:", " ".join(map(str, fibonacci_series(n))))

if __name__ == "__main__":
    main()