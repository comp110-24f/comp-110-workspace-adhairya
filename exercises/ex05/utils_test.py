"""Unit tests for list utility functions"""

__author__ = "730744596"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import add_at_index
import pytest


def test_only_evens_edge() -> None:
    """tests only_evens with an empty list"""
    a: list[int] = []
    assert len(only_evens(a)) == 0  # if its an empty list then its length should be 0


def test_only_evens_return() -> None:
    "tests only evens return with a sample mixture of odd and even numbers"
    a: list[int] = [1, 2, 3, 4, 6, 7]  # an input list with odd and even numbers
    function_result: list[int] = only_evens(a)
    expected_function_result: list[int] = [
        2,
        4,
        6,
    ]  # the expected result of the function

    for i in range(
        len(function_result)
    ):  # checks if the result of the function matches with the expected result by going through each element
        assert function_result[i] == expected_function_result[i]


def test_only_evens_mutation() -> None:
    """tests that the input list stays the same by running only_evens then comparing the values of the input list with an exact copy"""
    a: list[int] = [1, 2, 3, 4, 6, 7]  # the input list
    b: list[int] = [
        1,
        2,
        3,
        4,
        6,
        7,
    ]  # the expected result (a copy of the input list since it isnt mutating)
    only_evens(a)
    for i in range(len(a)):
        assert (
            a[i] == b[i]
        )  # goes through each element of the lists to ensure that the input list wasnt modified by matching with its exact duplicate


def test_sub_edge() -> None:
    """tests sub with an empty list"""
    a: list[int] = []
    assert len(sub(a, 0, 1)) == 0  # if its an empty list then its length should be 0


def test_sub_return() -> None:
    """tests sub with a random list of integers to see if the return value is the wanted subset"""
    a: list[int] = [1, 2, 3, 4, 6, 7]  # the input list
    function_result: list[int] = sub(
        a, 1, 3
    )  # running the functino sub and getting a subset
    expected_function_result: list[int] = [2, 3]  # the expected list
    for i in range(
        len(function_result)
    ):  # for loop comparing the values of the function return with that of the expected list one element at a time
        assert function_result[i] == expected_function_result[i]


def test_sub_mutation() -> None:
    """tests that input list stays the same even if sub is run with values"""
    a: list[int] = [1, 2, 3, 4, 6, 7]  # the input list
    b: list[int] = [
        1,
        2,
        3,
        4,
        6,
        7,
    ]  # the expected result (a copy of the input list since it isnt mutating)
    sub(a, 1, 3)
    for i in range(
        len(a)
    ):  # goes through each index of both lists and compares values to ensure that they all math
        assert a[i] == b[i]


def test_add_at_index_edge() -> None:
    """checks if the index is valid in range of the input list"""
    with pytest.raises(IndexError):
        add_at_index(
            [1, 2, 3], 4, 5
        )  # sample  where since the list is length 3 the value 5 is out of range leading to indexError


def test_add_at_index_return() -> None:
    """checks if the wanted element is added at the intended index"""
    a: list[int] = [1, 2, 3, 4, 6]  # the input list
    add_at_index(a, 5, 4)  # inserts the value 5 at the index 4 using the function
    expected_function_result: list[int] = [1, 2, 3, 4, 5, 6]  # the expected list
    for i in range(
        len(a)
    ):  # uses a for loop to match each element of the expected result and the function result and sees if they match up
        assert a[i] == expected_function_result[i]


def test_add_at_index_mutation() -> None:
    """ensures that the input list mutated correctly"""
    a: list[int] = [1, 2, 3, 4, 5]  # input list
    add_at_index(a, 6, 5)  # inserts 6 at the index 5
    expected_function_result = [1, 2, 3, 4, 5, 6]  # the expected list
    for i in range(len(a)):  # uses a for lop to verify each element of both lists match
        assert a[i] == expected_function_result[i]
