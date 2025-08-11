def appendList(list1: list, list2: list) -> list:
    """
    Appends elements from list2 to list1 and returns the modified list1.

    Args:
        list1 (list): The list to which elements will be appended.
        list2 (list): The list containing elements to be appended to list1.

    Returns:
        list: The modified list1 with elements from list2 appended.
    """
    return list1 + list2


def concatenateList(lists: list) -> list:
    """
    Concatenates multiple lists into a single flattened list.

    Returns:
        list: A single list containing all elements from the input lists.
    """
    result = []
    for item in lists:
        result += item if isinstance(item, list) else [item]

    return result


def filterList(condition: callable, lst: list) -> list:
    """
    Filters elements in a list based on given predicate (condition).
    Args:
        condition (callable): A function that returns True for elements to keep.
        lst (list): The list to be filtered.
    Returns:
        list: A new list containing elements that satisfy the condition.
    """

    return [item for item in lst if condition(item)]


