def check_common_elements(set1: set, set2: set) -> bool:
    """
    Check if two sets have any common elements.
    Args:
        set1 (set): First set of numbers
        set2 (set): Second set of numbers
    Returns:
        bool: True if sets have common elements, False otherwise
    """
    for i in set1:
        if i in set2 :
            return True
        
    return False
a={1,2,33,7,55,6}
b={12345,5432,1,23,4,4}
print(check_common_elements(a,b))

