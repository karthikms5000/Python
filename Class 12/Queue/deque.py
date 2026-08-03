#!/usr/bin/env python3
"""
Double-Ended Queue (Deque) Implementation using a standard Python list.

The Deque class holds only data-manipulation logic (no I/O). All user-facing
output and input handling live in the menu functions, which also validate
input and unwind cleanly on Ctrl+C / Ctrl+D.

Compatible with Python 3.14.6.
"""


class ExitProgram(Exception):
    """Raised to unwind all menus and exit the program cleanly."""


class Deque:
    """A double-ended queue backed by a Python list. Logic only, no I/O."""

    def __init__(self):
        self._items = []

    def is_empty(self):
        """Return True if the deque has no elements."""
        return len(self._items) == 0

    def insert_front(self, element):
        """Insert an element at the front of the deque."""
        self._items.insert(0, element)

    def insert_rear(self, element):
        """Insert an element at the rear of the deque."""
        self._items.append(element)

    def deletion_front(self):
        """Remove and return the front element.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Queue underflow: cannot delete from an empty deque.")
        return self._items.pop(0)

    def deletion_rear(self):
        """Remove and return the rear element.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Queue underflow: cannot delete from an empty deque.")
        return self._items.pop()

    def get_front(self):
        """Return the front element without removing it.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Queue underflow: deque is empty.")
        return self._items[0]

    def get_rear(self):
        """Return the rear element without removing it.

        Raises:
            IndexError: If the deque is empty.
        """
        if self.is_empty():
            raise IndexError("Queue underflow: deque is empty.")
        return self._items[-1]

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)


# --- I/O helpers -------------------------------------------------------

def safe_input(prompt):
    """Read a line of input, raising ExitProgram on Ctrl+C / Ctrl+D."""
    try:
        return input(prompt)
    except (EOFError, KeyboardInterrupt):
        raise ExitProgram from None


def prompt_element(prompt):
    """Prompt for a non-blank element, reprompting until one is given."""
    while True:
        value = safe_input(prompt).strip()
        if value:
            return value
        print("Input cannot be blank. Please enter a value.")


def display_deque(my_deque):
    """Print the current state of the deque."""
    print(f"Current Deque (Front to Rear): {my_deque}")


# --- Menus ---------------------------------------------------------------

def normal_queue_menu():
    """Sub-menu for using the deque as a normal Queue (FIFO)."""
    my_deque = Deque()
    print("\n--- Normal Queue Mode (FIFO: Enqueue Rear, Dequeue Front) ---")

    while True:
        print("\nOperations:")
        print("1. Enqueue (Insert at Rear)")
        print("2. Dequeue (Delete from Front)")
        print("3. Peek Front")
        print("4. Check if Empty")
        print("5. View Queue State")
        print("6. Return to Main Menu")

        choice = safe_input("Enter your choice (1-6): ").strip()

        if choice == "1":
            elem = prompt_element("Enter element to enqueue: ")
            my_deque.insert_rear(elem)
            print(f"Inserted {elem} at the rear.")
            display_deque(my_deque)
        elif choice == "2":
            try:
                elem = my_deque.deletion_front()
                print(f"Deleted {elem} from the front.")
            except IndexError as exc:
                print(exc)
            display_deque(my_deque)
        elif choice == "3":
            try:
                front = my_deque.get_front()
                print(f"Front element: {front}")
            except IndexError as exc:
                print(exc)
        elif choice == "4":
            print("Queue is empty." if my_deque.is_empty() else "Queue is not empty.")
        elif choice == "5":
            display_deque(my_deque)
        elif choice == "6":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


def complete_deque_menu():
    """Sub-menu for using the deque as a complete Deque."""
    my_deque = Deque()
    print("\n--- Complete Deque Mode (Double-Ended Operations) ---")

    while True:
        print("\nOperations:")
        print("1. Insert at Front")
        print("2. Insert at Rear")
        print("3. Delete from Front")
        print("4. Delete from Rear")
        print("5. Get Front Element")
        print("6. Get Rear Element")
        print("7. Check if Empty")
        print("8. View Deque State")
        print("9. Return to Main Menu")

        choice = safe_input("Enter your choice (1-9): ").strip()

        if choice == "1":
            elem = prompt_element("Enter element to insert at front: ")
            my_deque.insert_front(elem)
            print(f"Inserted {elem} at the front.")
            display_deque(my_deque)
        elif choice == "2":
            elem = prompt_element("Enter element to insert at rear: ")
            my_deque.insert_rear(elem)
            print(f"Inserted {elem} at the rear.")
            display_deque(my_deque)
        elif choice == "3":
            try:
                elem = my_deque.deletion_front()
                print(f"Deleted {elem} from the front.")
            except IndexError as exc:
                print(exc)
            display_deque(my_deque)
        elif choice == "4":
            try:
                elem = my_deque.deletion_rear()
                print(f"Deleted {elem} from the rear.")
            except IndexError as exc:
                print(exc)
            display_deque(my_deque)
        elif choice == "5":
            try:
                front = my_deque.get_front()
                print(f"Front element: {front}")
            except IndexError as exc:
                print(exc)
        elif choice == "6":
            try:
                rear = my_deque.get_rear()
                print(f"Rear element: {rear}")
            except IndexError as exc:
                print(exc)
        elif choice == "7":
            print("Deque is empty." if my_deque.is_empty() else "Deque is not empty.")
        elif choice == "8":
            display_deque(my_deque)
        elif choice == "9":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")


def main():
    """Main program entry point with interactive command-line interface."""
    print("==========================================")
    print("   Double-Ended Queue (Deque) Program     ")
    print("==========================================")

    try:
        while True:
            print("\nMain Menu:")
            print("1. Use/test as a normal Queue")
            print("2. Use/test as a complete Deque")
            print("3. Exit Program")

            choice = safe_input("Enter your choice (1-3): ").strip()

            if choice == "1":
                normal_queue_menu()
            elif choice == "2":
                complete_deque_menu()
            elif choice == "3":
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice! Please enter 1, 2, or 3.")
    except ExitProgram:
        print("\nExiting program. Goodbye!")


if __name__ == "__main__":
    main()
