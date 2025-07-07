from math import floor, log


def isArmstrong(input: int) -> bool:
    """
    Check if an input is Armstrong numbers.

    An Armstrong number is a number that is equal to the sum of its own digits
    raised to the power of the number of digits.

    Args:
    x (int): An integer to check.
    """
    if input < 0:
        raise ValueError("Input cannot be negative")

    k = floor(log(input, 10) + 1)
    digits = [int(digit) for digit in str(input)]

    return input == sum(int(digit) ** k for digit in digits)
