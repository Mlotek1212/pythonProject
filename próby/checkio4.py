"""Dowiedz się, ile zer znajduje się na końcu liczby.

Wejście: Dodatni Int

Wyjście: Int."""
def end_zeros(a: int) -> int:
    count = 0
    while a % 10 == 0:
        if a == 0:
            return count
        count += 1
        a //= 10

    return count

def end_zeros_new(a: int) -> int:
    for count, char in enumerate(str(a)[::-1]):
        if char != "0":
            return count
    return count + 1






print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
# assert end_zeros(0) == 1
# assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")