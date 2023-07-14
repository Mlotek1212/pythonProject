def is_last_item(items: list, i: int) -> bool:
    return i == len(items) - 1


def max_profit_more_equal_than_zero(itmes: list) -> int:
    result = max(itmes) if itmes else 0
    return result if result > 0 else 0


def stock_profit(stock: list[int]) -> int:
    profit = []
    for i, price in enumerate(stock):
        if is_last_item(stock, i):
            continue
        max_price_available = max(stock[i + 1:])
        profit.append(max_price_available - price)
    return max_profit_more_equal_than_zero(profit)



print("Example:")
# print(stock_profit([3,]))
# print(stock_profit([3, 1, 3, 4, 5, 1]))
#
# # These "asserts" are used for self-checking
# assert stock_profit([2, 3, 4, 5]) == 3
# assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
assert stock_profit([4, 3, 2, 1]) == 0
assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
assert stock_profit([1, 1, 1, 1]) == 0

print("You are the best broker here! Click 'Check' to earn cool rewards!")
