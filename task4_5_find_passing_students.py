def find_passing_students(names: list, scores: list, passing_score: int = 60) -> list:
    """
    Find which students passed using names and scores.
    Args:
        names (list): List of student names
        scores (list): List of corresponding scores
        passing_score (int): Minimum score to pass, defaults to 60
    Returns:
        list: List of names of students who passed
    """
    l=[]
    for i,n in zip(names,scores):
        if n>=60:
           l.append((i,n))
    return l
a=['jonibek','otabek','sardor']
b=[10,99,72]
print(find_passing_students(a,b))