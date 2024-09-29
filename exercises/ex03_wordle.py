"""EX03 - Structured Wordle"""

__author__ = "730744596"


def input_guess(secret_word_len: int) -> str:
    """Function that ensures that the length of the guess of someone playing the game matches with the length of the secret word"""
    word_choice: str = input(f"Enter a {secret_word_len} character word: ")
    while len(word_choice) != secret_word_len:
        # A while loop that checkes if the length of a users guess is not equal to that of the secret word
        print(f"That wasn't {secret_word_len} chars! Try again:")
        word_choice = input()
        # The while loop repeatedly asks for input of a new guess until the length matches the length of the secret word
    return word_choice


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Fucntion that checks if a specific letter of a users guess matches with some letter in the secret word"""
    assert len(char_guess) == 1
    # This ensures that the letter is only one character or else it results in an assertion error
    index_search: int = 0
    while index_search < len(secret_word):
        # Loops through the secret word for the character and once one instance is found it returns true
        if secret_word[index_search] == char_guess:
            return True
        index_search += 1
        # If an instance of the character isnt found then the index_search value increments 1 so that the full secret word can be looked through
    return False


def emojified(guess: str, secret: str) -> str:
    """Function that shows the user if a letter in their guess exists in the secret word and/or if it is in the right place in the guess"""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # These are the different color boxes that are printed to show if the letter exists/is in its intended location
    assert len(guess) == len(secret)

    emojified_result: str = ""
    # This is the string that prints out with the color of boxes once every letter in the guess is checked
    index: int = 0

    while index < len(guess):
        # Every letter in the guess is checked with this while loop
        if guess[index] == secret[index]:
            emojified_result += GREEN_BOX
            # If the letter at the index in guess matches with the letter at the index in secret this adds a green box to the result
        elif contains_char(secret, guess[index]):
            emojified_result += YELLOW_BOX
            # If the letter at the index in the guess doesnt match with the letter at the index in secret but it EXISTS in the secret word then the results adds a yellow box
        else:
            emojified_result += WHITE_BOX
            # If the letter doesnt exist at all then the white box is added to the result
        index += 1
        # This is responsible for incrementing through the guess so that every letter is checked with the condtions above
    return emojified_result


def main(secret: str) -> None:
    """This functions purpose is to run the game by keeping track of turns and if the user wins. This manages the flow of the game."""
    maximum_turns: int = 6
    turns_lapsed: int = 0
    won_game: bool = False
    # We begin with the conditions where the player only has 6 turns, has 0 turns elapsed until the first input is entered, and finally the game is not won yet so it is False
    while turns_lapsed < maximum_turns and won_game == False:
        # The while loop keeps looping through as long as turns_lapsed is less than the maximum turns allowed, and the game has not been won
        turns_lapsed += 1
        print(f"=== Turn {turns_lapsed}/{maximum_turns} ===")
        # This keeps track of the amount of turns lapsed and ensures the user knows how many turns they have used
        guess: str = input_guess(len(secret))
        print(emojified(guess, secret))
        # These ask the user for a guess each time and print the emojified result

        if guess == secret:
            won_game = True
        # Eventually if the game is won, and the turns_lapsed < maximum turns then the following statemnts printed below otherwise if it isnt achieved then another message is conveyed

    if won_game == True:
        print(f"You won in {turns_lapsed}/{maximum_turns} turns!")
    else:
        print(f"X/{maximum_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
