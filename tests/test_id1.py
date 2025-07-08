from exercises.id1 import sum_multiplier_v1, sum_multiplier_v2


def test1_sum_multiplier_v1() -> None:
    assert 23 == sum_multiplier_v1(10)


def test2_sum_multiplier_v1() -> None:
    assert 233168 == sum_multiplier_v1(1000)


def test_sum_multiplier_v2() -> None:
    assert sum_multiplier_v1(1000) == sum_multiplier_v2(1000)


def test3_sum_multiplier_v1() -> None:
    assert [0, 23, 2318, 233168, 23331668, 2333316668, 233333166668] == [
        sum_multiplier_v1(int(pow(10, i))) for i in range(0, 7)
    ]
