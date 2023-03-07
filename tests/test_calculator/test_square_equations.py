from calculator.square_equations import first_place_zero, second_place_zero, calculate_delta


def test_first_place_zero():
    assert first_place_zero(1, 4, 4) == -1


def test_second_place_zero():
    assert second_place_zero(1, 4, 4) == -3


def test_calculate_delta():
    assert calculate_delta(1, 4, 3) == 4
