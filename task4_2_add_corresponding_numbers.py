def add_corresponding_numbers(list1: list, list2: list) -> list:
    """
    Add corresponding numbers from two lists.
    Args:
        list1 (list): First list of numbers
        list2 (list): Second list of numbers
    Returns:
        list: List containing sum of corresponding numbers
    """
    a=[]
    for i,n in zip(list1,list2):
        a.append((i+n))
    return a
s=[1,2,3,4,5]
d=[1,2,3,4,5]
print(add_corresponding_numbers(s,d))
