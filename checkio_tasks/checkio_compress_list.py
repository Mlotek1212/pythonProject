from collections.abc import Iterable


def compress(items: list[int]) -> Iterable[int]:
    results = []
    for i,item in enumerate(items):
        print(i, item)
        if i == 0 or item != results[-1]:
            results.append(item)
            # print('abc')
            yield item
            # print('111')


# def compress(items: list[int]) -> Iterable[int]:
#     results = []
#     for i,item in enumerate(items):
#         print(i, item)
#         if i == 0 or item != results[-1]:
#             results.append(item)
#     return results


# for item in compress([5,5,5,6]):
#     print(item)




print("Example:")
print(list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])))

# These "asserts" are used for self-checking
assert list(compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])) == [
    5,
    4,
    5,
    6,
    5,
    7,
    8,
    0,
]
assert list(compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])) == [1, 2, 1]
assert list(compress([7, 7])) == [7]
assert list(compress([])) == []
assert list(compress([1, 2, 3, 4])) == [1, 2, 3, 4]
assert list(compress([9, 9, 9, 9, 9, 9, 9])) == [9]
assert list(compress([9, 9, 9, 9, 9, 9, 9, 0, 9, 9, 9, 9, 9, 9])) == [9, 0, 9]