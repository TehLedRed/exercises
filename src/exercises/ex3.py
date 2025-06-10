import math


def isArmstrong(input: int) -> bool:
    """
    Check if a given list of integers are Armstrong numbers.

    An Armstrong number is a number that is equal to the sum of its own digits
    raised to the power of the number of digits.

    Args:
    x (list[int]): A list of integers to check.

    Returns:
    Generator: A generator object yielding True for Armstrong numbers and False
    for non-Armstrong numbers.

    Example:
    >>> list(isArmstrong__([153, 370, 371, 407]))
    [True, True, True, True]

    >>> list(isArmstrong__([1634, 8208, 9474, 54748]))
    [True, True, True, True]

    >>> list(isArmstrong__([1633, 8209, 9475, 54749]))
    [False, False, False, False]
    """
    if not input or not isinstance(input, int):
        raise ValueError("Input list cannot be empty")

    k = math.floor(math.log(input, 10) + 1)
    digits = [int(digit) for digit in str(input)]

    return input == sum([digit**k for digit in digits])
