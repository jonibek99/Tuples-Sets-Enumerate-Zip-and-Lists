def get_odd_indexed_items(items: list) -> list:
    """
    Print only items at odd indexes.
    Args:
        items (list): List of items
    Returns:
        list: Items at odd indexes
    """
    a=[]
    for i in range(len(items)):
        if i%2==0:
            a.append((items[i]))
    return a
b=[1,2,3,4,5]
print(get_odd_indexed_items(b))