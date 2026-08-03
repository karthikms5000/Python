def reverse_string_with_stack(text: str) -> str:
    """
    Reverse a string using a stack.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    stack = list(text)
    return "".join(stack.pop() for _ in range(len(stack)))