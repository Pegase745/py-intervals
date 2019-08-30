###############################################################
# This is a first attempt using a Binary Search Tree.         #
# It worked for a small number of ranges (<100k), but quickly #
# showed CPU limitations for the default of 1M ranges.        #
###############################################################

from random import randrange, randint
from typing import (
    cast,
    List,
    Tuple,
    NewType,
    Iterable,
    Generic,
    TypeVar,
    Optional,
)

DEFAULT_RANGES: int = 1000000
MAXIMUM_RANGE_ENDPOINT: int = 1000000000

# Define custom types
Range = NewType("Range", Tuple[int, int])
Point = NewType("Point", int)

T_Node = TypeVar("T_Node")
T_Tree = TypeVar("T_Tree")


class Node(Generic[T_Node]):
    """A tree's node implementation."""

    value: Point

    left: Optional[T_Node]

    right: Optional[T_Node]

    included_ranges: List[Range]

    def __init__(self, value: Point, ranges: List[Range]) -> None:
        """Initialize a node."""
        self.value = value
        self.included_ranges = ranges
        self.left = None
        self.right = None

    def find(self, value: Point, ranges: List[Range] = []) -> int:
        if self.value == value:
            return len(set(included_ranges(value, self.included_ranges)))
        elif self.value > value:
            if self.left:
                return self.left.find(value, self.included_ranges + ranges)
            else:
                return len(
                    set(included_ranges(value, self.included_ranges + ranges))
                )
        else:
            if self.right:
                return self.right.find(value, self.included_ranges + ranges)
            else:
                return len(
                    set(included_ranges(value, self.included_ranges + ranges))
                )


class Tree(Generic[T_Tree]):
    """A Binary Search Tree implementation."""

    root: Optional[Node]

    def __init__(self) -> None:
        self.root = None

    def set_root(self, value: Point, ranges: List[Range]) -> None:
        self.root = Node(value, ranges)

    def insert(self, value: Point, ranges: List[Range]) -> None:
        if self.root is None:
            self.set_root(value, ranges)
        else:
            parent = None
            current = self.root
            while current is not None:
                parent = current
                if current.value < value:
                    current = current.right
                else:
                    current = current.left

            if parent.value < value:
                parent.right = Node(value, ranges)
            else:
                parent.left = Node(value, ranges)

    def find(self, value):
        return self.root.find(value)


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


def create_random_ranges(nb_ranges: int) -> Tuple[List[Range], List[Point]]:
    """Create random ranges and construct an array of the sorted points."""
    ranges = []

    for n in range(nb_ranges):
        ranges.append(
            cast(
                Range,
                (
                    randrange(0, MAXIMUM_RANGE_ENDPOINT + 1),
                    randrange(0, MAXIMUM_RANGE_ENDPOINT + 1),
                ),
            )
        )

    start_points, end_points = cast(Tuple[Point, Point], zip(*ranges))
    iterable_points = cast(Iterable[Point], start_points + end_points)
    points = sorted(iterable_points)

    return ranges, points


def intersects(point: Point, range: Range) -> bool:
    """Check if a point intersects in a given range."""
    return range[0] <= point and point <= range[1]


def included_ranges(point: Point, ranges: List[Range]) -> List[Range]:
    """Return ranges where point intersects."""
    intersections = []

    for r in ranges:
        if intersects(point, r):
            intersections.append(r)

    return intersections


"""Run program."""
if __name__ == "__main__":
    try:
        # 1. Ask for a number of range
        input_ranges = prompt()

        # 2. Create random ranges with it sorted points
        ranges, points = create_random_ranges(input_ranges)

        # 3. Calculate the median point
        median = points[(len(points) - 1) // 2]

        # 4. Create a tree with the median as a root
        tree: Tree = Tree()
        tree.insert(median, included_ranges(median, ranges))

        # 5. Build the tree with the remaining points
        for i in points:
            tree.insert(i, included_ranges(i, ranges))

        # 6. Generate random numbers and find enclosures
        while True:
            randomInt = randint(0, MAXIMUM_RANGE_ENDPOINT)
            print(
                "{} => Enclosed by {} range(s)".format(
                    randomInt, tree.find(randomInt)
                )
            )
    except KeyboardInterrupt:
        pass
