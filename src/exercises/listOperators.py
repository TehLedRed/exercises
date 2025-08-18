from typing import Any, Callable


def appendList(
    lst1: list[Any],
    lst2: list[Any],
) -> list[Any]:
    """
    Given two lists, add all items in the second list to the end of the
    first list.
    """
    for item in lst2:
        lst1 = lst1 + [item]
    return lst1


def concatenateList(lst: list[Any]) -> list[Any]:
    """
    Concatenates multiple lists into a single flattened list.

    Returns:
        list: A single list containing all elements from the input lists.
    """
    result: list[Any] = []
    for item in lst:
        result += item if isinstance(item, list) else [item]

    return result


def filterList(
    condition: Callable[[Any], bool],
    lst: list[Any],
) -> list[Any]:
    """
    Filters elements in a list based on given predicate (condition).
    Args:
        condition (Callable): A function that returns True for elements to keep.
        lst (list): The list to be filtered.
    Returns:
        list: A new list containing elements that satisfy the condition.
    """

    return [item for item in lst if condition(item)]


def lengthList(lst: list[Any]) -> int:
    """
    Returns the length of a list.
    Args:
        lst (list): The list whose length is to be calculated.
    Returns:
        int: The length of the list.
    """
    return len(lst)


def mapList(
    function: Callable[[Any], [Any]],
    lst: list[Any],
) -> list[Any]:
    """
    Applies a function to each element of a list and returns a new list with the results.
    Args:
        function (Callable): The function to be applied to each element.
        lst (list): The list to which the function will be applied.
    Returns:
        list: A new list containing the results of applying the function to each element.
    """
    return [function(item) for item in lst]


def foldLeftList(
    function: Callable[[Any], [Any]],
    lst: list[Any],
    acc: int = 0,
) -> Any:
    """
    Applies a function to each element of a list, accumulating the result.
    Args:
        function (Callable): The function to be applied to each element.
        lst (list): The list to which the function will be applied.
        acc (int): The initial accumulator value.
    Returns:
        int: The final accumulated value after applying the function to all elements.
    """
    for item in lst:
        acc = function(acc, item)
    return acc


def reverseList(lst: list) -> list:
    """
    Reverses the order of elements in a list.
    Args:
        lst (list): The list to be reversed.
    Returns:
        list: A new list with elements in reverse order.
    """
    return lst[::-1]


def foldRightList(
    function: Callable[[Any], [Any]],
    lst: list,
    acc: int = 0,
) -> Any:
    """
    Applies a function to each element of a list, accumulating the result from right to left.
    Args:
        function (Callable): The function to be applied to each element.
        lst (list): The list to which the function will be applied.
        acc (int): The initial accumulator value.
    Returns:
        int: The final accumulated value after applying the function to all elements from right to left.
    """
    for item in reverseList(lst):
        acc = function(item, acc)
    return acc
