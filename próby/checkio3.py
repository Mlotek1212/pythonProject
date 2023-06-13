from functools import reduce



def multiplication_numbers(first, second):
    return first * second

def checkio(number: int) -> int:
    list = []
    i = 0
    while i < len(str(number)):
        if str(number)[i] != "0":
            list.append(int(str(number)[i]))

        i = i+1
    result = reduce(multiplication_numbers, list)
    return result


def checkio_new(number: int) -> int:
    if number == 0:
        return 0
    result = 1
    for item in str(number):
        if item == "0":
            continue
        result *= int(item)
    return result


print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1