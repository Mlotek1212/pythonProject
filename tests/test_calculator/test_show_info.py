from decimal import Decimal
from unittest import mock

from calculator.show_info import add_numbers, off, get_first_number, get_second_number, subtraction_numbers, \
    multiplication_numbers, sharing_numbers, compounding_numbers, pierwiastkowanie
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


def test_get_second_number():
    with mock.patch("calculator.show_info.input") as m_input:
        m_input.return_value = "1"
        result = get_second_number()
        assert type(result) == float
        assert result == 1.0


def test_subtraction_numbers_only_integer():
    result = subtraction_numbers(7, 2)
    assert result == 5
    assert type(result) == int


def test_subtraction_numbers_only_float():
    result = subtraction_numbers(9.05, 2.05)
    assert round(result, 2) == 7
    assert type(result) == float


def test_subtraction_numbers_different_types():
    result = subtraction_numbers(9, 2.47)
    assert round(result, 2) == 6.53
    assert type(result) == float


def test_multiplication_numbers():
    result = multiplication_numbers(2, 5)
    assert result == 10
    assert type(result) == int


def test_sharing_numbers_only_intiger():
    result = sharing_numbers(4, 2)
    assert result == 2
    assert type(result) == float


def test_sharing_numbers_only_float():
    result = sharing_numbers(4.5, 4.5)
    assert result == 1
    assert type(result) == float


def test_sharing_numbers_different_types():
    result = sharing_numbers(4.5, 2)
    assert result == 2.25
    assert type(result) == float


# def test_sharing_numbers_by_zero():
#     result = sharing_numbers(4, 0)


def test_compounding_numbers():
    result = compounding_numbers(6, 2)
    assert result == 36


def test_pierwiastkowanie():
    result = pierwiastkowanie(4, 2)
    assert result == 2
