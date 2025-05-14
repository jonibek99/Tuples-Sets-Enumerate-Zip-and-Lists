def remove_duplicates(numbers: list) -> set:
    """
    Remove duplicates from a list using a set.
    Args:
        numbers (list): A list of numbers with possible duplicates
    Returns:
        set: A set containing unique numbers from the input list
    """
    return  set(numbers)
a=[1,2,3,4,21,21,3,2312,2,121,2,1,21,2]
print(remove_duplicates(a))
