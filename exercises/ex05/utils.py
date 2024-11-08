"""EX05: Implementing list utility functions"""

__author__ = "730744596"


def only_evens(input: list[int]) -> list[int]:
    """returns a new list containing only the elements of the input lists that were even"""
    new_list: list[int] = []  # empty list to store even numbers
    for num in input:  # for loop for all the numbers in the input list
        if (num % 2) == 0:  # checks if number is even
            new_list.append(num)  # adds the even number to the new list

    return new_list  # function returns the list of even numbers


def sub(input: list[int], a: int, b: int) -> list:
    """generates a list which is a subset of the input list"""
    new_list: list[int] = []  # empty list to store the subset of numbers

    if (
        a < 0
    ):  # ensures that the start index is starting within bounds even if the given numbers less than 0
        a = 0
    if b > len(
        input
    ):  # ensures that the end index doesnt exceed the maximum length of the list
        b = len(input)

    if (
        len(input) == 0 or a >= len(input) or b <= 0
    ):  # deals with cases where the input list is empty or the index are out of the valid value range
        return new_list

    # for loop to append each value between the intended range to the empty list
    for i in range(a, b):
        new_list.append(input[i])

    return new_list  # returns the subset of the input list


def add_at_index(input: list[int], a: int, b: int) -> None:
    """modifies the input list to place the wanted element at the wanted index"""

    # checks if the index given is within the range
    if b < 0 or b > len(input):
        raise IndexError("Index is out of bounds for the input list")

    input.append(0)  # adds an element to the end as a placeholder
    index_set: int = (
        len(input) - 2
    )  # start loop from the second to last element as the placeholder was added
    while (
        index_set >= b
    ):  # shifts elements to the right by making the value next to the index equal to the one to the left
        input[index_set + 1] = input[index_set]
        index_set -= 1
    input[b] = a  # inserts the wanted element at the wanted index
