"""EX03 - list Utility Functions"""

__author__ = "730744596"


def all(list: list[int], comparevalue: int) -> bool:
    for number in list:
        if number != comparevalue:
            return False
    return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    largest: int = input[0]
    for number in input:
        if number > largest:
            largest = number
    return largest
