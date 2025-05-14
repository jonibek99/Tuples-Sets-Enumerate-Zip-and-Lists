def sort_descending(numbers: list) -> list:
    """
    Sort a list in descending order.
    Args:
        numbers (list): List of numbers to sort
    Returns:
        list: List sorted in descending order
    """
    return sorted(numbers)[::-1]
a=[12,23,23,99999,31121,33,23,23,1,1,12,]
print(sort_descending(a))