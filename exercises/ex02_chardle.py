"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730744596"


def main() -> None:
    """Defines the main function which is the main entry point for the program"""
    # From the signature the return value is None so the type is Nonetype
    word: str = input_word()
    letter = input_letter()
    contains_char(word, letter)

    # Calls contains_char with the argument word being the return value of input_word and the argument letter being the return value of input_letter


def input_word() -> str:
    """Defines a function input_word that takes in no parameters as input"""
    word_choice: str = input("Enter a 5-character word: ")
    if len(word_choice) < 5 or len(word_choice) > 5:
        print("Error: Word must contain 5 characters.")
        exit()
    else:
        print(word_choice)
    return word_choice
    # The function asks for a 5 character word and then uses an if conditional to determine if it is 5 chars (or more or less)
    # The return value is word_choice if the word ends up being 5 characters


def input_letter() -> str:
    "Defines a function input_letter that takes in no parameters"
    letter_choice: str = input("Enter a single character: ")
    if len(letter_choice) < 1 or len(letter_choice) > 1:
        print("Error: Character must be a single character.")
        exit()
    else:
        print(letter_choice)
    return letter_choice
    # The function askes for 1 character and then uses an if condtional to determine if it is 1 char (or more or less)
    # The return value is letter_choice if the letter ends up being 1 character


def contains_char(word: str, letter: str) -> None:
    """Defines a function contains_char that takes in the stings word and letter as input"""

    print("Searching for " + letter + " in " + word)
    count: int = 0

    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    # Checks for a match between a letter and the letter at a certain index of the word
    # Then it prints "letter found at index 0,1,2,3 or 4 if there is a match and adds 1 to the count of times the letter is found

    if count == 0:
        print("No instances of " + letter + " found in " + word)

    elif count == 1:
        print("1 instance of " + letter + " found in " + word)

    else:
        print(str(count) + " instances of " + letter + " found in " + word)

    # This if conditional prints a statement for the number of instances a letter is found in a word. If there is zero it displays "No instances"


if __name__ == "__main__":
    main()
