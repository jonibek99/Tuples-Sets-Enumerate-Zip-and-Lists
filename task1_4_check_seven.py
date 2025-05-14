def check_seven(numbers: tuple) -> bool:
    """
    Check if the number 7 exists in a tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        bool: True if 7 is in the tuple, False otherwise
    """
    if 7 in numbers:
        return True
    return False
a=2,3,4,5,5,6
print(check_seven(a))