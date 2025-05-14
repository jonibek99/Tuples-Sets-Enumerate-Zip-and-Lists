def remove_first(lst: list) -> list:
    """
    Remove the first element from a list.
    Args:
        lst (list): The input list
    Returns:
        list: List with the first element removed
    """
    return lst[1:]
a=[1,12,2,12,2,3]
print(remove_first(a))