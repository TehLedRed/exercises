from exercises.rationalNumber import rationalNumber

# Equality


def test_equality_first() -> None:
    assert rationalNumber(2, 4) == rationalNumber(2, 4)


def test_equality_second() -> None:
    assert rationalNumber(2, 4) == rationalNumber(1, 2)


def test_equality_third() -> None:
    assert rationalNumber(5, 3) != rationalNumber(2, 4)


# Addiction


def test_add_two_positive_rationalNumber_numbers() -> None:
    assert rationalNumber(1, 2) + rationalNumber(2, 3) == rationalNumber(7, 6)


def test_add_a_positive_rationalNumber_number_and_a_negative_rationalNumber_number() -> None:
    assert rationalNumber(1, 2) + rationalNumber(-2, 3) == rationalNumber(-1, 6)


def test_add_two_negative_rationalNumber_numbers() -> None:
    assert rationalNumber(-1, 2) + rationalNumber(-2, 3) == rationalNumber(-7, 6)


def test_add_a_rationalNumber_number_to_its_additive_inverse() -> None:
    assert rationalNumber(1, 2) + rationalNumber(-1, 2) == rationalNumber(0, 1)


# Subtraction


def test_subtract_two_positive_rationalNumber_numbers() -> None:
    assert rationalNumber(1, 2) - rationalNumber(2, 3) == rationalNumber(-1, 6)


def test_subtract_a_positive_rationalNumber_number_and_a_negative_rationalNumber_number() -> None:
    assert rationalNumber(1, 2) - rationalNumber(-2, 3) == rationalNumber(7, 6)


def test_subtract_two_negative_rationalNumber_numbers() -> None:
    assert rationalNumber(-1, 2) - rationalNumber(-2, 3) == rationalNumber(1, 6)


def test_subtract_a_rationalNumber_number_from_itself() -> None:
    assert rationalNumber(1, 2) - rationalNumber(1, 2) == rationalNumber(0, 1)


# Multiplication


def test_multiply_two_positive_rationalNumber_numbers() -> None:
    assert rationalNumber(1, 2) * rationalNumber(2, 3) == rationalNumber(1, 3)


def test_multiply_a_negative_rationalNumber_number_by_a_positive_rationalNumber_number() -> None:
    assert rationalNumber(-1, 2) * rationalNumber(2, 3) == rationalNumber(-1, 3)


def test_multiply_two_negative_rationalNumber_numbers() -> None:
    assert rationalNumber(-1, 2) * rationalNumber(-2, 3) == rationalNumber(1, 3)


def test_multiply_a_rationalNumber_number_by_its_reciprocal() -> None:
    assert rationalNumber(1, 2) * rationalNumber(2, 1) == rationalNumber(1, 1)


def test_multiply_a_rationalNumber_number_by_1() -> None:
    assert rationalNumber(1, 2) * rationalNumber(1, 1) == rationalNumber(1, 2)


def test_multiply_a_rationalNumber_number_by_0() -> None:
    assert rationalNumber(1, 2) * rationalNumber(0, 1) == rationalNumber(0, 1)


# Division


def test_divide_two_positive_rationalNumber_numbers() -> None:
    assert rationalNumber(1, 2) / rationalNumber(2, 3) == rationalNumber(3, 4)


def test_divide_a_positive_rationalNumber_number_by_a_negative_rationalNumber_number() -> None:
    assert rationalNumber(1, 2) / rationalNumber(-2, 3) == rationalNumber(-3, 4)


def test_divide_two_negative_rationalNumber_numbers() -> None:
    assert rationalNumber(-1, 2) / rationalNumber(-2, 3) == rationalNumber(3, 4)


def test_divide_a_rationalNumber_number_by_1() -> None:
    assert rationalNumber(1, 2) / rationalNumber(1, 1) == rationalNumber(1, 2)


# Tests of type: Absolute value


def test_absolute_value_of_a_positive_rationalNumber_number() -> None:
    assert abs(rationalNumber(1, 2)) == rationalNumber(1, 2)


def test_absolute_value_of_a_positive_rationalNumber_number_with_negative_numerator_and_denominator() -> (
    None
):
    assert abs(rationalNumber(-1, -2)) == rationalNumber(1, 2)


def test_absolute_value_of_a_negative_rationalNumber_number() -> None:
    assert abs(rationalNumber(-1, 2)) == rationalNumber(1, 2)


def test_absolute_value_of_a_negative_rationalNumber_number_with_negative_denominator() -> (
    None
):
    assert abs(rationalNumber(1, -2)) == rationalNumber(1, 2)


def test_absolute_value_of_zero() -> None:
    assert abs(rationalNumber(0, 1)) == rationalNumber(0, 1)


def test_absolute_value_of_a_rationalNumber_number_is_reduced_to_lowest_terms() -> None:
    assert abs(rationalNumber(2, 4)) == rationalNumber(1, 2)


# Tests of type: Exponentiation of a rationalNumber number


def test_raise_a_positive_rationalNumber_number_to_a_positive_integer_power() -> None:
    assert rationalNumber(1, 2) ** 3 == rationalNumber(1, 8)


def test_raise_a_negative_rationalNumber_number_to_a_positive_integer_power() -> None:
    assert rationalNumber(-1, 2) ** 3 == rationalNumber(-1, 8)


def test_raise_a_positive_rationalNumber_number_to_a_negative_integer_power() -> None:
    assert rationalNumber(3, 5) ** -2 == rationalNumber(25, 9)


def test_raise_a_negative_rationalNumber_number_to_an_even_negative_integer_power() -> None:
    assert rationalNumber(-3, 5) ** -2 == rationalNumber(25, 9)


def test_raise_a_negative_rationalNumber_number_to_an_odd_negative_integer_power() -> None:
    assert rationalNumber(-3, 5) ** -3 == rationalNumber(-125, 27)


def test_raise_zero_to_an_integer_power() -> None:
    assert rationalNumber(0, 1) ** 5 == rationalNumber(0, 1)


def test_raise_one_to_an_integer_power() -> None:
    assert rationalNumber(1, 1) ** 4 == rationalNumber(1, 1)


def test_raise_a_positive_rationalNumber_number_to_the_power_of_zero() -> None:
    assert rationalNumber(1, 2) ** 0 == rationalNumber(1, 1)


def test_raise_a_negative_rationalNumber_number_to_the_power_of_zero() -> None:
    assert rationalNumber(-1, 2) ** 0 == rationalNumber(1, 1)


# Tests of type: Exponentiation of a real number to a rationalNumber number


def test_raise_a_real_number_to_a_positive_rationalNumber_number() -> None:
    assert 8 ** rationalNumber(4, 3) == 15.999999999999998


def test_raise_a_real_number_to_a_negative_rationalNumber_number() -> None:
    assert 9 ** rationalNumber(-1, 2) == 0.3333333333333333


def test_raise_a_real_number_to_a_zero_rationalNumber_number() -> None:
    assert 2 ** rationalNumber(0, 1) == 1.0


# Tests of type: Reduction to lowest terms


def test_reduce_a_positive_rationalNumber_number_to_lowest_terms() -> None:
    assert rationalNumber(2, 4) == rationalNumber(1, 2)


def test_reduce_places_the_minus_sign_on_the_numerator() -> None:
    assert rationalNumber(3, -4) == rationalNumber(-3, 4)


def test_reduce_a_negative_rationalNumber_number_to_lowest_terms() -> None:
    assert rationalNumber(-4, 6) == rationalNumber(-2, 3)


def test_reduce_a_rationalNumber_number_with_a_negative_denominator_to_lowest_terms() -> None:
    assert rationalNumber(3, -9) == rationalNumber(-1, 3)


def test_reduce_zero_to_lowest_terms() -> None:
    assert rationalNumber(0, 6) == rationalNumber(0, 1)


def test_reduce_an_integer_to_lowest_terms() -> None:
    assert rationalNumber(-14, 7) == rationalNumber(-2, 1)


def test_reduce_one_to_lowest_terms() -> None:
    assert rationalNumber(13, 13) == rationalNumber(1, 1)