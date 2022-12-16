
def add_number(value_1, value_2=None):
    result = value_1 + value_2
    print(f"{result=}")
    return result


def sum_result_items(items: list) -> int | float:
    result = 0
    for item in items:
        result = add_number(result, item)
    print(f"Excepted {result=}")
    return result


# result = 0
# result += add_number(3, 5)
# result += add_number(3, 2)
# result += add_number(13, 5)
# print(result)

# result2 = 0
# result2 = add_number(result2, 5)
# result2 = add_number(result2, 2)
# result2 = add_number(result2, 8)
#
# print(f"Excepted {result2=}")


print('NAME!!!!', __name__)
if __name__ == '__main__':
    sum_result_items([5, 2, 8])
    sum_result_items([5, 22, 8])




