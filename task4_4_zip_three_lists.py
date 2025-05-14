def zip_three_lists(list1: list, list2: list, list3: list) -> list:
    """
    Zip three lists together.
    Args:
        list1 (list): First list
        list2 (list): Second list
        list3 (list): Third list
    Returns:
        list: List of tuples containing items from all three lists
    """
    a=[]
    for i,n,m in zip(list1,list2,list3):
        a.append((i,n,m))
    return a
list1=['jonibek','otabek','sardor']
list2=['100','21','21']
list3=['azizivich','azizivich','sardor']
print(zip_three_lists(list1,list2,list3))