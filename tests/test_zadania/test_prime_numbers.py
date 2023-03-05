import pytest

from zadania.prime_numbers import get_prime_number_from_range, number_of_divisors


@pytest.mark.parametrize(
    "range_from, range_to, excepted",
    [
        (1, 1, []),
        (1, 2, [2]),
        (1, 5, [2, 3, 5]),
        (3, 5, [3, 5])


    ]
)
def test_for_one_number(range_from, range_to, excepted):
    assert get_prime_number_from_range(range_from, range_to) == excepted

@pytest.mark.parametrize(
    "number, excepted",
    [
        (1, 1),
        (10, 4),
        (100, 9),
    ]
)
def test_number_of_divisors(number, excepted):
    assert number_of_divisors(number) == excepted