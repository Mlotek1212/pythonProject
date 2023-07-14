from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:
    if len(elements) == 0:
        return True
    fires_element = elements[0]
    for item in elements[1:]:
        if item != fires_element:
            return False
    return True


    return True


print("Example:")
print(all_the_same([1, 1, 1]))

# These "asserts" are used for self-checking
assert all_the_same([1, 1, 1]) == True
assert all_the_same([1, 2, 1]) == False
assert all_the_same([1, "a", 1]) == False
assert all_the_same([1, 1, 1, 2]) == False
assert all_the_same([]) == True
assert all_the_same([1]) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
