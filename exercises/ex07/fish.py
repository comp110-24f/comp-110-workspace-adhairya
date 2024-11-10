"""File to define Fish class."""


class Fish:
    """Class representing the fish that live in the river."""

    age: int
    # attribute

    def __init__(self):
        """Initial constructor."""
        self.age = 0
        return None

    def one_day(self):
        """One day of life in the river for the fish."""
        self.age += 1  # each day the age increases by 1
        return None
