"""Implementing list utility functions"""

__author__ = "730744596"


def only_evens(input: list[int]) -> list[int]:
    new_list: list[int] = []
    for num in input:
        if (num % 2) == 0:
            new_list.append(num)

    return new_list


def sub(input: list[int], a: int, b: int) -> list:
    new_list: list[int] = []

    if a < 0:
        a = 0
    if b > len(input):
        b = len(input)

    if len(input) == 0 or a >= len(input) or b <= 0:
        return input

    for i in range(a, b):
        new_list.append(input[i])

    return new_list


def add_at_index(input: list[int], a: int, b: int) -> None:

    if b < 0 or b > len(input):
        raise IndexError("Index is out of bounds for the input list")

    input.append(0)
    index_set: int = len(input) - 2
    while index_set >= b:
        input[index_set + 1] = input[index_set]
        index_set -= 1
    input[b] = a
