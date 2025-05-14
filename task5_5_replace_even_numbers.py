def replace_even_numbers(numbers: list) -> list:
    """
    Replace all even numbers with 0.
    Args:
        numbers (list): List of integers
    Returns:
        list: List with even numbers replaced by 0
    """
    a=[]
    for i in numbers:
       if i%2==0:
           a.append(0)
       else:
           a.append(i)
    return a
s=[2,3,4,4,1,6]
print(replace_even_numbers(s))

