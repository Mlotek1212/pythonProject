from collections.abc import Iterable


class Engine:
    manufacture = 'DE'

    def __init__(self, **kwargs):
        self.amount_piston = kwargs.get('amount_piston')
        self.oil = kwargs.get('oil')
        self.capacity = kwargs.get('capacity')


#
#
engines = [
    Engine(amount_piston=4, oil='5W40', capacity=1950),
    Engine(amount_piston=2, oil='5W40', capacity=1950),
    Engine(amount_piston=4, capacity=1950)
]


#
#
# def sorting_key(obj: Engine) -> tuple:
#     return obj.manufacture != 'DE', obj.oil


def sorting_key(obj: list) -> tuple:
    # (-1, 4)
    # (-1, 5)
    # (-2, 2)
    return -len(obj), obj[0]


def frequency_sorting(numbers: list[int]) -> Iterable[int]:
    number_count = {}
    for number in numbers:
        if not number in number_count.keys():
            number_count[number] = [number]
        else:
            number_count[number].append(number)
    result = number_count.values()
    result = sorted(result, key=sorting_key)
    # [[1], [2], [3,3]] -> [1,2,3,3]
    # [1] +  [1] -> [1,1]
    new_result = []
    for items in result:
        new_result += items
    print(new_result)

    return new_result


print("Example:")
# print(list(frequency_sorting([1, 2, 3, 4, 5])))
# print(list(frequency_sorting([5, 5, 3, 2, 4, 1])))

# These "asserts" are used for self-checking
assert list(frequency_sorting([1, 2, 3, 4, 5])) == [1, 2, 3, 4, 5]
assert list(frequency_sorting([3, 4, 11, 13, 11, 4, 4, 7, 3])) == [
    4,
    4,
    4,
    3,
    3,
    11,
    11,
    7,
    13,
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
