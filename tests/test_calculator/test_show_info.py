from unittest import mock

from calculator.show_info import add_numbers, off, get_first_number
import pytest


def test_add_numbers_only_integer():
    result = add_numbers(1, 2)
    assert result == 3
    assert type(result) == int


def test_add_numbers_only_float():
    result = add_numbers(1.01, 2.53)
    assert result == 3.54
    assert type(result) == float


def test_add_numbers_different_types():
    result = add_numbers(1, 2.53)
    assert result == 3.53
    assert type(result) == float


def test_off_not_implemented_error():
    with pytest.raises(NotImplementedError) as exc:
        off(1, 2)

    assert "Wyłączenie kalkulatora" in str(exc)


def test_get_first_number():
    with mock.patch("calculator.show_info.input") as m_input:
        m_input.return_value = "1"
        result = get_first_number()
        assert type(result) == float
        assert result == 1.0


