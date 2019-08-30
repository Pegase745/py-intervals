import random
from intervals import create_random_range, MAXIMUM_RANGE_ENDPOINT


def test_create_random_range_ok():
    """Return a valid random range."""
    start, end = create_random_range()

    assert start >= 0
    assert start < end
    assert end <= MAXIMUM_RANGE_ENDPOINT


def test_start_smaller_end_ok(monkeypatch):
    """Check that start is always smaller than end."""
    random_numbers = [10, 8, 12]

    def randrange(x: int, _):
        return random_numbers.pop(0)

    monkeypatch.setattr(random, "randrange", randrange)

    start, end = create_random_range()

    assert start == 10
    assert end == 12


def test_no_range_one_element_ok(monkeypatch):
    """Check that there is no range of one element."""
    random_numbers = [10, 10, 12]

    def randrange(x: int, _):
        return random_numbers.pop(0)

    monkeypatch.setattr(random, "randrange", randrange)

    start, end = create_random_range()

    assert start == 10
    assert end == 12
