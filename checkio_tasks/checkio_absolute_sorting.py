
# this is few example of using key function usable by sorted
# def my_key(value):
#     if value < -10:
#         return abs(value)
#     if value < 11:
#         return value * 2
#     if value < 20:
#         return value *0.5
#     return abs(value)


def checkio(values: list) -> list:
    return sorted(values, key=abs)
    # other solutions useful for learning
    # values.sort(key=abs)
    # return values
    # return sorted(values, key=my_key)
    # return sorted(values, key=lambda value: value * 5 if value < 10 else abs(value))


print("Example:")
print(checkio([-20, -5, 10, 15]))

# These "asserts" are used for self-checking
assert checkio([-20, -5, 10, 15]) == [-5, 10, 15, -20]
assert checkio([1, 2, 3, 0]) == [0, 1, 2, 3]
assert checkio([-1, -2, -3, 0]) == [0, -1, -2, -3]

print("The mission is done! Click 'Check Solution' to earn rewards!")