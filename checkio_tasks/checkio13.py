def checkio(data: list[int]) -> int | float:
    data.sort()
    amount_numbers = len(data)
    if amount_numbers == 1:
        print(data)
        return data[0]
    else:
        center_nuber = amount_numbers / 2
        if amount_numbers % 2 != 0:
            center_nuber = round(center_nuber + 0.1)
            return data[center_nuber - 1]
        else:
            center_nuber = round(center_nuber)
            median_numbers = data[center_nuber - 1: center_nuber + 1]
            return sum(median_numbers) / 2
    #
    # elif  == 1:
    #     breakpoint()
    #     split1 = round(len(data) / 2)
    #     median = data[split1 - 1: split1 + 1]
    #     print(sum(median) / 2)
    #     return sum(median) / 2
    # else:
    #     x = round((len(data) / 2) + 0.01)
    #     split = round((len(data) / 2) + 0.01)
    #     print(data[split - 1])
    #     return data[split -1 ]



# print("Example:")
# print(checkio([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert checkio([1, 2, 3, 4, 5]) == 3
assert checkio([3, 1, 2, 5, 3]) == 3
assert checkio([1, 300, 2, 200, 1]) == 2
assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
assert checkio([33, 56, 62]) == 56
assert checkio([21, 56, 84, 82, 52, 9]) == 54
assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
assert checkio([64, 6, 92, 7, 70, 5]) == 35.5
# #
# print("The mission is done! Click 'Check Solution' to earn rewards!")