def get_prime_number_from_range(range_from: int, range_to: int) -> list[int]:
    numbers = range(range_from, range_to + 1)
    results = []
    for number in numbers:
        if number_of_divisors(number) == 2:
            results.append(number)

    return results

    # return [number for number in numbers if number_of_divisors(number) == 2]


def number_of_divisors(number: int) -> int:
    amount = 0
    for check_number in range(1, number + 1):
        if number % check_number == 0:
            amount += 1
    return amount
    # return sum([1 for check_number in range(1, number + 1) if number%check_number == 0])
