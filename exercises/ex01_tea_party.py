"""Program to plan a cozy tea party"""

__author__ = "730744596"


def main_planner(guests: int) -> None:
    """Defines the main function which is the main entry point for the program"""
    # From the signature the return value is None and so the type is Nonetype
    print("A Cozy Tea Party for " + str(guests) + " People!")

    print("Tea Bags: " + str(tea_bags(people=guests)))
    # Calls 'tea_bags(people=guests)'and returns 'people*2'
    # Converts the return value to a string and prints 'Tea Bags: guests*2'

    print("Treats: " + str(treats(people=guests)))
    # Calls 'treats(people=guests)'and returns '1.5 * tea_bags(people=guests)'
    # Converts the return value to a string and prints 'Treats: 1.5 * tea_bags(people=guests)'

    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))
    # Calls cost(tea_bags(people=guests), treats(people=guests) and returns '(0.75 * treats(people=guests)) + (0.5 * tea_bags(people=guests))'
    # Converts the return value to a string and prints 'Cost: $0.75 * treats(people=guests)) + (0.5 * tea_bags(people=guests)'


def tea_bags(people: int) -> int:
    """Defines a function 'tea_bags' that takes in an integer 'people' as input"""
    return people * 2

    # The return value is 'people * 2'. Where 'people' is the value held by the local variable and then passed to the caller.


def treats(people: int) -> int:
    """Defines a function 'treats' that takes an integer 'people' as input.
    It calls 'tea_bags' with 'people' as the argument for 'people' and recieves the return value for 'tea_bag'
    """
    return int(1.5 * tea_bags(people=people))

    # Calls 'tea_bags(people = people)', the return value of 'tea_bags' is then multiplied by 1.5 and then converted to an integer.


def cost(teacount: int, treat_count: int) -> float:
    """Defines a function 'cost' that takes an integer 'teacount' and an integer 'treat_count' as input."""
    return (0.75 * treat_count) + (0.5 * teacount)

    # The return value is '0.75*treat_count + "0.5*tea_count'. Where 'treat_count' and 'tea_count' is the value helped by the local variable and then passed to the caller.


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
# Calls the 'main_planner' function to start the program.
# 'Main' takes 'guest' as an input which is asked by the question: 'How many guests are attending your tea party?'
