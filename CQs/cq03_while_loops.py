"""Writing a while loop to iterate over a string in COMP 110!"""

__author__ = "730744596"


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    index_number: int = 0

    while index_number < len(phrase):
        if phrase[index_number] == search_char:
            count += 1
        index_number += 1

    return count
