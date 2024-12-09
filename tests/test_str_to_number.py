import pytest
from my_pyutils.str_to_number import str_to_number


def test_str_to_number():
    # Test integer conversion
    assert str_to_number("123") == 123
    assert isinstance(str_to_number("123"), int)

    # Test float conversion
    assert str_to_number("12.34") == 12.34
    assert isinstance(str_to_number("12.34"), float)

    # Test invalid input
    assert str_to_number("abc") is None
    assert str_to_number("12.34.56") is None
    assert str_to_number("") is None