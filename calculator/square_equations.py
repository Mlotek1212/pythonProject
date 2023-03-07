from calculator.cal import add_numbers, pierwiastkowanie, multiplication_numbers, subtraction_numbers
from calculator.show_info import compounding_numbers


def zero_place(
        a: int | float,
        b: int | float,
        delta: int | float,
        is_first_place: bool,
) -> int | float:
    if is_first_place:
        fun = add_numbers
    else:
        fun = subtraction_numbers
    return fun(-b, pierwiastkowanie(delta, 2)) / multiplication_numbers(2, a)


def first_place_zero(
        a: int | float,
        b: int | float,
        delta: int | float,
) -> int | float:
    return zero_place(a, b, delta, is_first_place=True)


def second_place_zero(
        a: int | float,
        b: int | float,
        delta: int | float,
) -> int | float:
    return zero_place(a, b, delta, is_first_place=False)


def calculate_delta(a: int | float, b: int | float, c: int | float) -> int | float:
    return subtraction_numbers(compounding_numbers(b, 2), multiplication_numbers(4, multiplication_numbers(a, c)))
