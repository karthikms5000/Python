class OddStack:
    """A stack that stores only odd integers."""

    def __init__(self):
        self._items = []

    def push(self, item):
        """Push an odd integer onto the stack."""
        if not isinstance(item, int):
            raise TypeError("Only integers can be added.")

        if item % 2 == 0:
            raise ValueError("Only odd integers are allowed.")

        self._items.append(item)

    def pop(self):
        """Remove and return the top element."""
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

    def display(self):
        """Return a copy of the stack."""
        return self._items.copy()

    def __len__(self):
        return len(self._items)


def main():
    stack = OddStack()

    print("=== Odd Number Stack Program ===")
    print("Enter odd integers. Type 'done' to finish.\n")

    while True:
        user_input = input("Enter a number: ").strip()

        if user_input.lower() == "done":
            break

        try:
            number = int(user_input)
            stack.push(number)
            print(f"✓ {number} added to the stack.")

        except ValueError as e:
            print(f"✗ {e}")

        except TypeError as e:
            print(f"✗ {e}")

    if stack.is_empty():
        print("\nThe stack is empty.")
        return

    print("\nStack (bottom → top):", stack.display())

    # Find the largest value by popping elements
    largest = stack.pop()

    while not stack.is_empty():
        current = stack.pop()
        if current > largest:
            largest = current

    print("Largest odd number:", largest)


if __name__ == "__main__":
    main()