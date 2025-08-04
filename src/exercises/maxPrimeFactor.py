def maxPrimeFactor(n: int) -> int:
    """
    Find the max_prime_factor prime factor of a number.

    Args:
    n (int): An integer.

    Return:
    An integer.
    """
    if n <= 1:
        raise ValueError("n must be greater than 1!")

    max_prime_factor = 2
    while n % 2 == 0:
        max_prime_factor = 2
        n //= 2

    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            max_prime_factor = i
            n //= i

    return max(n, max_prime_factor)


# Pseudo algorithm
# Input: n
# dividend = n
# max_prime_factor = 2
# Loop over prime numbers up to n
# For divisor in sequence of prime numbers list
#     if dividend % divisor == 0:
#         max_prime_factor = divisor
#         dividend //= divisor
# return max_prime_factor
