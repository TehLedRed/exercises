def sum_multiplier_v1(max: int = 10) -> int:
    """
    Calculates the sum of all numbers below 'max' that are multiples of 3 or 5.

    Source: https://projecteuler.net/problem=1

    Args:
        max (int): An integer with default set to 10.

    Return: An integer.
    """
    cum_sum = 0
    for number in range(1, max):
        if number % 3 == 0 or number % 5 == 0:
            cum_sum += number
    print(max)
    return cum_sum


def sum_multiplier_v2(max: int = 10) -> int:
    return sum(number for number in range(1, max) if number % 3 == 0 or number % 5 == 0)
