def find_union(set1: set, set2: set) -> set:
    """
    Find the union of two sets.
    Args:
        set1 (set): First set of numbers
        set2 (set): Second set of numbers
    Returns:
        set: Union of both sets
    """
    set1=list(set1)
    set2=list(set2)
    return set(set1+set2)
a=[1,2,3,4,4,5,5]
b=[12,3,12,31,3,23,2,32]
print(find_union(a,b))
