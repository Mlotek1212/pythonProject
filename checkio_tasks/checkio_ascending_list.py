# def is_ascending(items: list[int]) -> bool:
#     result = []
#     for item in items:
#         result.append(item)
#         if item < result[-1]:
#             result.append(item)
#         else:
#             return False
#     return True


def is_ascending(items: list[int]) -> bool:
    previous_item = None
    for item in items:
        if previous_item and item <= previous_item:
            return False
        previous_item = item
    return True


print("Example:")
print(is_ascending([-5, 10, 99, 123456]))

# These "asserts" are used for self-checking
assert is_ascending([-5, 10, 99, 123456]) == True
assert is_ascending([99]) == True
assert is_ascending([4, 5, 6, 7, 3, 7, 9]) == False
assert is_ascending([]) == True
assert is_ascending([1, 1, 1, 1]) == False
assert is_ascending([1, 3, 3, 5]) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
