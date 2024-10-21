__author__ = "730744596"

from CQs.cq07.find_max import find_and_remove_max


def test_expected_value() -> None:
    a: list[int] = [9, 8, 7, 9]
    assert find_and_remove_max(a) == 9


def test_mutation() -> None:
    a: list[int] = [9, 8, 7, 9]
    find_and_remove_max(a)
    assert a == [8, 7]


def test_edge_casese() -> None:
    a: list[int] = []
    assert find_and_remove_max(a) == -1
