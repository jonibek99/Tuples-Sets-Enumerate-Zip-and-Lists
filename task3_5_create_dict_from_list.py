def create_dict_from_list(items: list) -> dict:
    """
    Create a dictionary from a list using enumerate.
    Args:
        items (list): List of items
    Returns:
        dict: Dictionary with indices as keys and items as values
    """
    return dict(enumerate(items))
a=['jonibek',12,'me','you']
print(create_dict_from_list(a))