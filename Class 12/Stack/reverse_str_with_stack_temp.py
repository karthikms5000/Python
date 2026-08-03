def reverse_string_with_stack(text: str) -> str:
    """
    Reverse a string using a stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if len(text) < 2:
        return text

    char_stack = list(text)
    reversed_chars: list[str] = []

    while char_stack:
        reversed_chars.append(char_stack.pop())

    return "".join(reversed_chars)


def main() -> None:
    original = "Python 3.14 Stack"
    reversed_text = reverse_string_with_stack(original)

    print(f"Original : {original}")
    print(f"Reversed : {reversed_text}")


if __name__ == "__main__":
    main()