"""EX06: Practice with dictionary functions"""

__author__ = "730744596"


def invert(a: dict[str, str]) -> dict[str, str]:
    """A function the inverts the keys and the values of a dictionary"""
    new_dict: dict[str, str] = (
        {}
    )  # initalizes an empty dictionary to store the new pairs of values: keys
    for index in a:  # iterates over each key in the original dictionary
        if (
            a[index] in new_dict
        ):  # checks for duplicate keys by looking at the value and seeing if it is a key in the new dictionary
            raise KeyError
        new_dict[a[index]] = (
            index  # sets the original key of the dictionary to the value in the new dictionary
        )
    return new_dict  # returns the inverted dictionary


def favorite_color(a: dict[str, str]) -> str:
    """returns the color that appears most frequently"""

    if len(a) == 0:  # cheks if the dictionary is empty
        return ""

    color_count: dict[str, int] = (
        {}
    )  # intitalizes a dictionary which keeps track of the frequency of a color like color: frequency
    for name in a:  # loops through the colors in the original dictionary
        color = a[name]
        if (
            color in color_count
        ):  # checks to see if the color already exists in the new dictionary
            color_count[
                color
            ] += 1  # if it does then the frequency count value is incremented by 1
        else:  # if the color doesnt exist already then it is added to the dictionary and set to a value of 1
            color_count[color] = 1

    maximum: int = 0  # keeps track of the color with the highest frequency value
    color_popular: str = ""  # sotres the most popular color
    for color_name in color_count:  # loops through the colors of the dictionary
        if (
            color_count[color_name] > maximum
        ):  # checks if the frequency has increased in value for the color
            maximum = color_count[
                color_name
            ]  # updates the maximum frequency value encountered
            color_popular = color_name  # sets the popular color to the color encountered at this maimum frequency

        elif (
            color_count[color_name] == maximum and color_popular == ""
        ):  # checks for duplicates and sets the popular color to the first instance
            color_popular = color_name

    return color_popular  # returns the most popular color


def count(a: list[str]) -> dict[str, int]:
    """Counts the number of times a value appears in a list"""
    new_dictionary: dict[str, int] = (
        {}
    )  # initalizes an empty dictionary to record the amount of times a certain value appears
    for elem in a:  # loops through each element of the lists
        if (
            elem in new_dictionary
        ):  # sees if that element is already a key in the dictionary
            new_dictionary[elem] += 1  # if it is the count is incremented by one
        else:
            new_dictionary[elem] = (
                1  # if the element isnt a key already then it is added as a key and the value is set to a count of 1
            )
    return new_dictionary  # the new dictionary created is then returned


def alphabetizer(a: list[str]) -> dict[str, list[str]]:
    """Function that assigns a list of words to a letter based on the first letter of words"""
    new_dictionary: dict[str, list[str]] = (
        {}
    )  # initalizes an empty dictionary to store the list of words in the form of letter: list of words

    for elem in a:  # loops through each element of the input list
        if (
            elem[0] in new_dictionary
        ):  # checks if the character is already a key in the dictionary
            new_dictionary[elem[0].lower()].append(
                elem
            )  # if so the the element (word) is added to the list of values associated with that key
        else:
            new_dictionary[elem[0].lower()] = [
                elem
            ]  # else if the character isnt already a key then it is added as a key to the dictionary and the word that prompted that key will be assigned the first value in the list

    return (
        new_dictionary  # returns the dictionary with the characters and list of words
    )


def update_attendance(a: dict[str, list[str]], b: str, c: str) -> None:
    """Mutates an original dictionary to add values to the list which is the value of the dicitonary"""
    if b in a:  # checks if the day already exists in the dictionary
        if c in a[b]:  # checks if the value already exists in this list
            return None
        a[b].append(
            c
        )  # if so the the name is appeneded to the list that already exists with that day
    else:
        a[b] = [
            c
        ]  # else if the day doesnt exist in the dictionary then it is added and set to the name of that student given
