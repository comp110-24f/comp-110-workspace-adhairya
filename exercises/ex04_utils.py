"""EX03 - list Utility Functions"""

__author__ = "730744596"


def all(list: list[int], comparevalue: int) -> bool:
    """This function checks if all of the integers in a list are the same as a given integer"""
    if len(list) == 0:
        return False
    # If the list is empty then we return false
    for number in list:
        if number != comparevalue:
            return False
        # Using a for loop this function returns false if any number in the list does not match the integer we are comparing values with
    return True
    # If the for loop completes without finding an instance where a number doesnt equal the compared value then True is returned


def max(input: list[int]) -> int:
    """This function finds the largest value in a list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    # If the list is empty this statement is returned stating that the list is empty
    largest: int = input[0]
    # This assumes that the largest number is the first number in the list
    for number in input:
        if number > largest:
            largest = number  # This updates largest if a larger number is found using this if conditional

    return (
        largest  # This returns the largest number found after the for loop is completed
    )


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """This function checks if two lists of integers are equal"""
    if len(list1) != len(list2):
        return False
    # This checks if the lists are the same size and if they are not it returns False
    for index in range(len(list1)):
        if list1[index] != list2[index]:
            return False
    # This for loop compares every value of list 1 and list 2 and if at any point they dont match it returns false otherwise it returns true
    return True


def extend(a: list[int], b: list[int]) -> None:
    """This function mutates values from one list of ints to a second list of ints"""
    for number in b:
        a.append(
            number
        )  # every value of b is appended to list a through this for loop where it goes through all the values of b and then appends it to a
