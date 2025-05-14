def replace_with_index(items: list) -> list:
    """
    Replace items in a list with their index using enumerate.
    Args:
        items (list): List of items to be replaced with indices
    Returns:
        list: List with items replaced by their indices
    """
    a=[]
    for i in enumerate(items):
        a.append((i[0]))
    return a
a=[1,2,3,4,5,6,7,8,9]
print(replace_with_index(a))