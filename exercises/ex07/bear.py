"""File to define Bear class."""


class Bear:
    """Class that represents the bears that live by the river."""

    age: int
    hunger_score: int
    # attributes

    def __init__(self):
        """Initital constructor."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """One day of life of the bears."""
        self.age += 1  # increases the age by 1
        self.hunger_score -= 1  # decreases the hunger score by 1
        return None

    def eat(self, num_fish: int) -> None:
        """Tracks the amount of fish the bear eats."""
        self.hunger_score += (
            num_fish  # hunger score goes up by the amount of fish the bear eats
        )
        return None
