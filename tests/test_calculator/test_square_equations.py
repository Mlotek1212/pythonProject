import pytest

from calculator.square_equations import first_place_zero, second_place_zero, calculate_delta, calculate_square_equations


def test_first_place_zero():
    assert first_place_zero(1, 4, 4) == -1


def test_second_place_zero():
    assert second_place_zero(1, 4, 4) == -3


def test_calculate_delta():
    assert calculate_delta(1, 4, 3) == 4


def test_calculate_delta_zero_place_zero():
    with pytest.raises(ValueError) as exc:
        calculate_delta(1, 1, 1)

    assert "delta can`t be less than zero" in str(exc)


def test_calculate_square_equations_one_place():
    assert calculate_square_equations(1, 4, 4) == (-2,)


def test_calculate_square_equations_two_place():
    assert calculate_square_equations(-1, 8, -12) == (2, 6)


def test_calculate_square_equations_zero_place():
    assert calculate_square_equations(1, 4, 5) == tuple()
