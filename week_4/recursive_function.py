def add_numbers(values: list[int]) -> int:
    # 1. values = [3, 4, 57, 23]
    # 2. values = [4, 57, 23]
    # 3. values = [57, 23]
    # 4. values = [23]
    # 5. values = [] -> 0
    print(values)
    if not values:
        return 0
    return values[0] + add_numbers(values[1:])  # 3 + add_numbers([4, 57, 23])


def should_add_first_item(value: int, *, is_even: bool, is_positive: bool) -> bool:
    if is_positive == False and value > 0:
        return False
    elif is_positive == True and value <= 0:
        return False
    return (is_even and not value % 2) or (not is_even and value % 2)


def add_even_or_odd_numbers(values: list[int], is_even: bool, is_positive=None) -> int:
    """
    is_even = True -> parzyste
    is_even = False -> nie parzyste -> odd
    """
    if not values:
        return 0
    if should_add_first_item(
        value=values[0],
        is_even=is_even,
        is_positive=is_positive,
    ):
        return values[0] + add_numbers(values[1:])
    return add_numbers(values[1:])  # 3 + add_numbers([4, 57, 23])


def add_even_numbers(values: list[int]) -> int:
    return add_even_or_odd_numbers(values=values, is_even=True)


def add_odd_numbers(values: list[int]) -> int:
    return add_even_or_odd_numbers(values=values, is_even=False)


def add_odd_positive_numbers(values: list[int]) -> int:
    return add_even_or_odd_numbers(values=values, is_even=False, is_positive=True)


def add_odd_negative_numbers(values: list[int]) -> int:
    return add_even_or_odd_numbers(values=values, is_even=False, is_positive=False)


def add_odd_positive_numbers(values: list[int]) -> int:
    return add_even_or_odd_numbers(values=values, is_even=False, is_positive=True)


def add_even_negative_numbers(values: list[int]) -> int:
    return add_even_or_odd_numbers(values=values, is_even=False, is_positive=False)


def add_even_numbers(values: list[int]) -> int:
    # 1. values = [3, 4, 57, 23] -> 3 jest nieprzyste -> nie dodajemy tego
    # 2. values = [4, 57, 23] -> 4 jes parzyste -> dodajemy
    # 3. values = [57, 23] -> 57 jest nieparzyst -> nie dodajemy
    # 4. values = [23] -> 23 jest nieparzyst -> nie dodajemy
    # 5. values = [] -> 0
    print(values)
    if not values:
        return 0
    if not values[0] % 2:
        return values[0] + add_numbers(values[1:])  # 3 + add_numbers([4, 57, 23])
    return add_numbers(values[1:])  # 3 + add_numbers([4, 57, 23])


def add_odd_numbers(values: list[int]) -> int:
    # 1. values = [3, 4, 57, 23] -> 3 jest nieprzyste -> dodajemy
    # 2. values = [4, 57, 23] -> 4 jes parzyste -> nie dodajemy
    # 3. values = [57, 23] -> 57 jest nieparzyst -> dodajemy
    # 4. values = [23] -> 23 jest nieparzyst -> dodajemy
    # 5. values = [] -> 0
    print(values)
    if not values:
        return 0
    if values[0] % 2:
        return values[0] + add_numbers(values[1:])  # 3 + add_numbers([4, 57, 23])
    return add_numbers(values[1:])  # 3 + add_numbers([4, 57, 23])



    # return values[0] + add_numbers(values[1:2]+ add_numbers(values[2:3]+ add_numbers(values[3:4]
    # return values[0] + values[1] + values[2] + values[3] + values[4]

sum_result = add_numbers([3, 4, 57, 23])
sum_result = add_numbers([3, 4, 57, 233, 4, 57, 233, 4, 57, 23])
# print("sum_result", sum_result)


def get_all_result_divided_value(value, divided):
    result = value / divided
    if int(result) <= 0:
        return 0
    print(f"{result=:.1f}")
    return get_all_result_divided_value(result, divided)


# get_all_result_divided_value(123445645674512345, 3)
get_all_result_divided_value(123445645674512345, 43)
