def count_threes(numbers: tuple) -> int:
    """
    Count how many times 3 appears in the tuple.
    Args:
        numbers (tuple): A tuple of integers
    Returns:
        int: The count of number 3 in the tuple
    """
    return numbers.count(3)
a=1,2,3,4,2,1,2,3,1
print(count_threes(a))
