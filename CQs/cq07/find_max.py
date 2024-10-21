__author__ = "730744596"


def find_and_remove_max(input: list[int]) -> int:

    if len(input) == 0:
        return -1

    largest: int = input[0]

    for number in input:
        if number > largest:
            largest = number

    index: int = 0
    while index < len(input):
        if input[index] == largest:
            input.pop(index)
        else:
            index += 1

    return largest
