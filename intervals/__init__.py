import random
from typing import Dict, Tuple
from collections import OrderedDict

DEFAULT_RANGES: int = 1000000
MAXIMUM_RANGE_ENDPOINT: int = 1000000000


def prompt() -> int:
    """Ask the user for a number of range."""
    msg: str = "How many ranges to generate - (default={}) \n".format(
        str(DEFAULT_RANGES)
    )
    while True:
        try:
            return int(input(msg) or DEFAULT_RANGES)
        except ValueError:
            raise ValueError("I only accept decimal numbers")


def create_random_range() -> Tuple[int, int]:
    """Create a random range.

    (start, end) where start < end, 0 <= start, end <= MAXIMUM_RANGE_ENDPOINT
    """
    start = random.randrange(0, MAXIMUM_RANGE_ENDPOINT + 1)
    end = 0
    exit = False

    while exit is not True:
        end = random.randrange(0, MAXIMUM_RANGE_ENDPOINT + 1)
        if start < end:
            exit = True

    return start, end


def create_ranges(nb_ranges: int) -> Dict[int, int]:
    """Create a given number of ranges."""
    ranges: Dict[int, int] = {}

    print(
        "Generating {} ranges... (it can take a few seconds)".format(nb_ranges)
    )

    for n in range(nb_ranges):
        start, end = create_random_range()
        ranges[start] = end

    return ranges


def get_nb_enclosures(value: int, ranges: Dict[int, int]) -> int:
    """Get the number of enclosures for a value in a list of ranges.

    Example:
        We want to search for 54 in the below
        ranges = {23: 55, 70: 101, 10: 60, 31: 52, 53: 90, 95: 102}

        Steps:
        1. filtered_dict = {23: 55, 10: 60, 31: 52, 53: 90}
        2. ordered_filtered_dict = {10: 60, 23: 55, 31: 52, 53: 90}
        3. enclosures = [60, 55, 90]
        4. result = 3
    """

    # Remove all entries where key (aka start point of a range) > value
    filtered_dict = {
        k: v for k, v in filter(lambda t: t[0] <= value, ranges.items())
    }

    # Create a new dict ordered by key ascending
    ordered_filtered_dict = OrderedDict(sorted(filtered_dict.items()))

    # Create an array of the end points of ranges where value < dict val
    enclosures = [
        v
        for _, v in filter(
            lambda t: t[1] >= value, ordered_filtered_dict.items()
        )
    ]

    return len(enclosures)


"""Main program."""
if __name__ == "__main__":
    try:
        # 1. Ask for a number of range
        input_ranges = prompt()

        # 2. Create random ranges
        ranges = create_ranges(input_ranges)

        # 3. Generate random numbers and find enclosures
        while True:
            random_int = random.randint(0, MAXIMUM_RANGE_ENDPOINT)

            result = get_nb_enclosures(random_int, ranges)

            print("{} => Enclosed by {} range(s)".format(random_int, result))
    except KeyboardInterrupt:
        pass
