from exercises.ex1 import encrypt


def test_encrypt() -> None:
    assert (
        encrypt("the quick brown fox jumps over the lazy dog")
        == "gsvjf rxpyi ldmul cqfnk hlevi gsvoz abwlt"
    )
