def index_power(ar: list[int], n: int) -> int:
    # list_power = []
    # for i, item in enumerate(ar):
    #     list_power
    #
    # return 0
    # print(list_power)
    if n < 0 or n >= len(ar):
        return -1
    return ar[n] ** n


print("Example:")
print(index_power([1, 2, 3], 2))

# These "asserts" are used for self-checking
assert index_power([1, 2, 3, 4], 2) == 9
assert index_power([1, 3, 10, 100], 3) == 1000000
assert index_power([0, 1], 0) == 1
assert index_power([1, 2], 3) == -1

print("The mission is done! Click 'Check Solution' to earn rewards!")