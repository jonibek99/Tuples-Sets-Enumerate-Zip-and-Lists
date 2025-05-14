def find_oldest(people: list) -> tuple:
    """
    Find the oldest person from a list of tuples (name, age).
    Args:
        people (list): List of tuples containing (name, age) pairs
    Returns:
        tuple: A tuple containing (name, age) of the oldest person
    """ 
    return max(people,key=lambda i: i[1] )
a = [('Jonibek', 99), ('Ali', 20), ('Olim', 22)]
print(find_oldest(a))