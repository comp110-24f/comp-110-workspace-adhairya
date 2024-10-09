"""Mutating functions."""

__author__ = "730744596"

list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1


def manual_append(list: list[int], appendval: int) -> None:
    list.append(appendval)


def double(list: list[int]) -> None:
    index: int = 0
    while index < len(list):
        list[index] *= 2
        index += 1


double(list_2)
print(list_1)
print(list_2)
