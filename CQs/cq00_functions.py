"""Practicing writing functions in COMP110!"""

__author__ = "730744596"


def mimic(message: str) -> str:
    """Function takes in your input and repeats it back to you"""
    return message


def main() -> None:
    """Prints results of calling mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
