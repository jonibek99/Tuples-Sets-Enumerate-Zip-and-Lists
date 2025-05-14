def count_apples(items: list) -> int:
    """
    Count how many times "apple" appears in a list.
    Args:
        items (list): List of strings
    Returns:
        int: Number of times "apple" appears in the list
    """
    return items.count('apple')
a=['apple','bodring','apple','apple','bodring','bodring']
print(count_apples(a))