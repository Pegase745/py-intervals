import pytest

from intervals import DEFAULT_RANGES, prompt


def test_prompt_ok(monkeypatch):
    """Return the given number of ranges."""
    monkeypatch.setattr("builtins.input", lambda x: "40")
    assert prompt() == 40


def test_prompt_with_no_input(monkeypatch):
    """Return the default number of ranges."""
    monkeypatch.setattr("builtins.input", lambda x: "")
    assert prompt() == DEFAULT_RANGES


def test_prompt_with_str_input(monkeypatch):
    """Raise ValueError if not an int."""
    monkeypatch.setattr("builtins.input", lambda x: "test")
    with pytest.raises(ValueError):
        assert prompt()
