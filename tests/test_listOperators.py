from exercises.listOperators import appendList, concatenateList, filterList

def test_appendList():
    assert appendList([1, 2], [3, 4]) == [1, 2, 3, 4]
    assert appendList([], [1, 2]) == [1, 2]
    assert appendList([1, 2], []) == [1, 2]
    assert appendList([], []) == []


def test_concatenateList():
    assert concatenateList([[1, 2], [3, 4], [5]]) == [1, 2, 3, 4, 5]
    assert concatenateList([[], [], []]) == []
    assert concatenateList([[1], [2], [3]]) == [1, 2, 3]
    assert concatenateList([]) == []


def test_filterList():
    assert filterList(lambda x: x > 0, [1, -2, 3, -4, 5]) == [1, 3, 5]
    assert filterList(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]) == [2, 4]
    assert filterList(lambda x: x < 0, [-1, -2, -3]) == [-1, -2, -3]
    assert filterList(lambda x: x > 0, []) == []
    assert filterList(lambda x: x % 2 == 0, []) == []
