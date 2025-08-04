from exercises.sumFibonacci import sumFibonacci, sumFibonacci2


def test_sum() -> None:
    assert  sumFibonacci(limit=4_000_000) == 4_613_732


def test_sum2() -> None:
    assert  sumFibonacci2(limit=4_000_000) == 4_613_732