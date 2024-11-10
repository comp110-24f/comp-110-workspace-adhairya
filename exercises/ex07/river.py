"""File to define River class."""

__author__ = "730744596"

from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear


class River:
    """Creating a river class with fish and bear type objects."""

    # attributes of the River class
    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Checks the age of the fish and bear."""
        new_fish_list: list[Fish] = []  # creates an empty list of type fish
        new_bear_list: list[Bear] = []  # creates an empty list of type bear
        for fish in self.fish:  # goes through each fish in the list of fish
            if fish.age <= 3:
                new_fish_list.append(
                    fish
                )  # if the fishes age is less than or equal to 3 then it is added to the new list of surviving fish
        self.fish = new_fish_list  # the original list is set to the new list

        for bear in self.bears:  # goes through each bear in the list of bears
            if bear.age <= 5:
                new_bear_list.append(
                    bear
                )  # if the bears age is less than or equal to 5 then it is added to the new list of surviing bears
        self.bears = new_bear_list  # sets the original list to the new list
        return None

    def bears_eating(self):
        """Calcuations for bear eating fish."""
        for bear in self.bears:  # goes through each bear in the list of Bears
            if len(self.fish) >= 5:  # checks the number of fish in the fish list
                self.remove_fish(3)  # removes 3 fish from the river
                bear.eat(3)  # calls the eat method for the bear to eat 3 fish
        return None

    def check_hunger(self):
        """Checks the hunger score of the bear."""
        new_bear_list: list[Bear] = (
            []
        )  # creates empty list to populate with surviving fish
        for bear in self.bears:  # checks each bear in the list of bears
            if (
                bear.hunger_score >= 0
            ):  # loops through to see the hunger score of each bear
                new_bear_list.append(
                    bear
                )  # if they survive they are appended to the new list
        self.bears = new_bear_list  # the new list is then set to the original list
        return None

    def repopulate_fish(self):
        """Repopulates the amount of fish in the river."""
        for i in range(
            0, (len(self.fish) // 2) * 4
        ):  # adds 4 fish for every multiple of 2 fish
            self.fish.append(
                Fish()
            )  # for the amount of fish it adds that many new fish
        return None

    def repopulate_bears(self):
        """Repopulates the amount of bears in the river."""
        for i in range(
            0, len(self.bears) // 2
        ):  # adds one bear for every pair of bears
            self.bears.append(
                Bear()
            )  # for the amount of bears calculated it adds that many bear objects
        return None

    def view_river(self):
        """Displays the amount of fish and bear in the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self) -> None:
        """Simulates one week of the simulation in the river."""
        for i in range(0, 7):  # dalls the one_river day function 7 times
            self.one_river_day()
        return None

    def remove_fish(self, amount: int) -> None:
        """Removes a certain amount of fish from the river."""
        for i in range(0, amount):
            self.fish.pop(i)
            # uses the pop method to remove the 1st fish and then go forward till the amounts reached
        return None
