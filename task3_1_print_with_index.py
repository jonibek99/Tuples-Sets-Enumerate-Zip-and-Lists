def print_with_index(items: list) -> None:
    """
    Use enumerate to print each item in a list with its index.
    Args:
        items (list): List of items to print with their indices
    Returns:
        None: Prints each item with its index
    """
    a=[]
    for i,t in enumerate(items):
        a.append((i,t))
    return a
a=[21212,323431,21413214,765432,1,323423]
print(print_with_index(a))