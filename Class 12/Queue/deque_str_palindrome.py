class Deque:
    def __init__(self):
        self.items = []

    def add_rear(self, item):
        self.items.append(item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop(0)

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def is_palindrome(text):
    # Create a deque
    dq = Deque()

    # Insert all characters into the deque
    for ch in text:
        dq.add_rear(ch)

    # Compare characters from both ends
    while dq.size() > 1:
        if dq.remove_front() != dq.remove_rear():
            return False

    return True


# Main Program
text = input("Enter a string: ")

if is_palindrome(text):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")