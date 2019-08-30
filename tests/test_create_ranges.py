import intervals


def test_create_ranges_ok(monkeypatch):
    """Return ranges for a given number."""
    random_ranges = [(23, 55), (70, 101), (10, 60)]

    monkeypatch.setattr(
        intervals, "create_random_range", lambda: random_ranges.pop(0)
    )

    result = intervals.create_ranges(3)

    assert result == {23: 55, 70: 101, 10: 60}
