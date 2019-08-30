import intervals


def test_get_nb_enclosures_ok():
    """Return number of enclosures of a value for given ranges."""
    val1 = 54
    val2 = 5

    ranges = {23: 55, 70: 101, 10: 60, 31: 52, 53: 90, 95: 102}

    result1 = intervals.get_nb_enclosures(val1, ranges)
    result2 = intervals.get_nb_enclosures(val2, ranges)

    assert result1 == 3
    assert result2 == 0
